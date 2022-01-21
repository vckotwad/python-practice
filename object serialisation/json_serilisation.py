import json
e={'name':'john','salary':'10000','ismarried':None}

#creating a json string
json_string=json.dumps(e,indent=4,sort_keys=True)
print(json_string)

#creatin a json file

with open('file.json','a') as f:
    json.dump(e,f)

#deserilisation
dict=json.loads(json_string)
print(dict)