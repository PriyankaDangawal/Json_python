import json

dict1='{"a": 1,"a":2,"a":3,"a": 4,"b": 1,"b":2}'
dict2=json.loads(dict1)
print("unique key of json",dict2)


