import json

data1={"name": "David",
     "class":"I",
     "age": None  
 }
out=json.dumps(data1)
with open("question3.json","w+") as f:
    f.write(out)

