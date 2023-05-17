import json
import pandas as pd
import re
#import couchdb
#from alcohol import detect_alcohol

with open('crime_data.csv', 'r') as file:
    crime_data = pd.read_csv(file, sep=',')

with open('twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    id_data = json.load(data_file)

def detect_alcohol(id_data, region):
    true_count= 0
    keywords = [
    "beer", "wine", "whiskey", "vodka", "gin", "rum", "tequila", "brandy", "cider", "sake", "mezcal",
    "liqueur", "champagne", "prosecco", "absinthe", "amaretto", "aperol", "baileys", "bourbon",
    "campari", "cognac", "daiquiri", "drambuie", "frangelico", "grappa", "jägermeister", "kahlua",
    "limoncello", "mead", "midori", "ouzo", "pimms", "port", "sambuca", "sherry", "sloe gin",
    "soju", "spirits", "vermouth", "whisky", "white russian", "absolut", "bacardi", "beefeater",
    "captain morgan", "cuervo", "disaronno", "glenfiddich", "grey goose", "hennessy", "jim beam",
    "johnnie walker", "martini", "moët & chandon", "patrón", "pernod", "seagrams", "smirnoff",
    "southern comfort", "stolichnaya", "tia maria", "wild turkey", "woodford reserve", "heineken",
    "corona", "guinness", "budweiser", "carlsberg", "modelo", "pilsner urquell", "sierra nevada",
    "stella artois", "asahi", "sapporo", "kirin", "tsingtao", "tiger beer", "san miguel", "chang beer",
    "singha beer", "yanjing beer", "bia hoi", "bia saigon", "bia ha noi", "bia 333", "bia larue", 
    "bia huda", "bia tiger", "bia 333", "bia truc bach", "bia halida", "bia hue", "bia da", "bia tuoi",
    "bia zorok", "bia phap", "bia bavaria", "bia hoegaarden", "bia tiger crystal", "bia 333 export",
    "bia leffe", "bia cuu long", "bia ba ba", "bia saigon special", "bia tiger fresh", "bia heineken 0.0",
    "bia sagota", "bia sai gon 9", "bia tuyp", "bia sai gon special export", "bia ha noi premium", 
    "bia hanoi", "bia hanoi beer", "bia hanoi gold", "bia saigon premium", "bia ho chi minh", 
    "bia ho chi minh city", "bia sài gòn tôm tắc", "bia tiger black", "bia ha noi dark", 
    "bia huda gold", "bia saigon special chill", "bia saigon red", "bia hanoi red", "bia tay", 
    "bia bia", "bia busch", "bia corona", "bia clara", "bia estrella", "bia gallo", "bia mahou", 
    "bia polar", "bia poker", "bia polar ice"]

    for i in id_data:
        for j in region:
            full_name = i['includes']['places'][0]['full_name'] 
            exact_name = full_name.lower().split(',')[0]
            if exact_name == j:
                for keyword in keywords:
                    if re.search(r'\b' + keyword + r'\b',i['data']['text'] , re.IGNORECASE):
                        true_count+=1
    return true_count



def get_total_offences(suburb, data):
    # 将输入的郊区名称转换为小写，以便进行大小写不敏感的匹配
    for i in suburb:
        one_suburb = i.lower()
    
        # 在 DataFrame 中进行筛选，并返回匹配的犯罪总数
        filtered_data = data[data['SUBURB'].str.lower() == one_suburb]
        if not filtered_data.empty:
            filtered_data = dict(filtered_data)
            total_offence = sum(filtered_data['\xa0total_offences'])
        num_alcohol = detect_alcohol(id_data, suburb)
        rate = num_alcohol/total_offence
        return rate






print(get_total_offences(['NORTH HAVEN'], crime_data))
