import json

data = open('./data.json', 'r').read()
data = json.loads(data)

for idx in range(len(data)):
    data[idx]['idx'] = idx
    
# encoding='UTF-8-sig' for korean
with open('data.json', 'w', encoding='UTF-8-sig') as file:
    json.dump(data, file, indent=4, ensure_ascii = False)
