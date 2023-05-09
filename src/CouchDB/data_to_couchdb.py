import couchdb
import json

def import_data_to_couchdb(file_path, masternode, user, password, database_name):
    # 构建CouchDB服务器URL
    url = f'http://{user}:{password}@{masternode}:5984/'

    # 连接到CouchDB服务器
    couchclient = couchdb.Server(url)

    # 创建或选择数据库
    db = couchclient.create(database_name) if database_name not in couchclient else couchclient[database_name]

    # 读取JSON文件并导入数据到CouchDB
    with open(file_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        for i in data:
            del i['_id']
            del i['_rev']
            db.save(i)

# 启动应用程序
if __name__ == "__main__":
    file_path = "./twitter-data-small.json"
    masternode = "172.26.133.182"
    user = 'admin'
    password = 'admin'
    database_name = 'twitter_full'
    import_data_to_couchdb(file_path, masternode, user, password, database_name)
