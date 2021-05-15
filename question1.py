import json

data={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }

file=open("question1.json","w")

json.dump(data,file)

file.close()


