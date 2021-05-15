import json

x={"name":"john","age":30,"city":"new yourk"}

file=json.dumps(x,indent=3)
with open("my.json","w+") as f:
    f.write(file)