import json
filename="text2.txt"
dict1={}
with open(filename) as fh:
    for line in fh:
        command,descripation=line.strip().split(None,1)
        dict1[command]+descripation.strip()
file=open("ques8.json","w")
json.dump(dict1,file,indent=6,sort_keys=True)
file.close()






