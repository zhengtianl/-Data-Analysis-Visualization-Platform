import json
with open('sentiment_result.json', 'r') as json_file:
    # Read the contents of the file
    json_result = json_file.read()
    # Parse the JSON data
    data_result = json.loads(json_result)

