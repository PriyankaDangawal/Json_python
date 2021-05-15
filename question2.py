import json    
     
data1={"name": "David",
     "class":"I",
     "age": 6  
 }
file=open("question2.json","r")
a=json.load(file)
print(a)
file.close()