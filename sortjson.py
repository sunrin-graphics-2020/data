import json
from collections import defaultdict

# tree -J work > filelist.json
data = open('filelist.json', 'r').read()
data = json.loads(data)
data = data[0]['contents']

jsonData = defaultdict(list)

for d in data:
    filelist = []
    for c in d['contents']:
        filelist.append(c['name'])
    jsonData[d['name']] = filelist
    
with open('file.json', 'w') as outfile:
    json.dump(jsonData, outfile, indent=4)