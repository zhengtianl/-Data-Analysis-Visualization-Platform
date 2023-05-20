import couchdb
import json
import os
import re
pattern = r'''includes":'''
def process_tweet(tweet_json,db):
    # 统一提取 user id 和fullname, text
    authorid = tweet_json['doc']['data']['author_id']
    text = tweet_json['doc']['data']['text']
    time = tweet_json['doc']['data']['created_at']
    try:
        #try
        fullname = tweet_json['doc']['includes']['places'][0]['full_name']
        simple_t = {'authorid':authorid,'text':text,'time':time,'place':fullname}
    except:
        simple_t = {'authorid':authorid,'text':text,'time':time}
    db.save(simple_t)
    return None


def portion_load(chunk_size, rank):
    # Connect to the CouchDB server
    couchclient = couchdb.Server('http://admin:admin@172.26.133.182:5984')
    # Create or open the database
    name='twitter_huge_loc_large'
    try:
        couchclient.create(name)
        db = couchclient[name]
    except: db = couchclient[name]
    

    # Calculate the start and end positions for each processor
    start_position = chunk_size*rank
    #确定结束为止 等同于下一个开始位置
    #end_position = chunk_size*(rank+1)
    line_count=1
    output_file = open('line.txt', 'w')
    f.seek(start_position)
    if rank == 0:
        f.readline()
    while True:
            new_line = f.readline()
            line_count += 1
            #if f.tell()>=end_position:
                #break
            if not new_line:
                 break
            if new_line.endswith('}'):
                 kk = new_line
            else:
                 kk = new_line[:-2]
            if re.search(pattern, kk):
                tweet_json = json.loads(kk)
                process_tweet(tweet_json,db)
                output_file.write(f"{line_count}\n")
        
    return None



# Set the number of processors to use
# Open the JSON file
with open('/data/mnt/ext100/twitter-huge.json', 'r') as f:
#with open('../test1.json', 'r') as f:

    # Get the total size of the file
    file_size = f.seek(0,2)
    size = 3
    # Calculate the size to read for each processor
    chunk_size = file_size // size
    print(chunk_size)
    portion_load(chunk_size,0)
  
