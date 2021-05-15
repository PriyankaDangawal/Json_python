# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. 
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
#  aur ye sab dictionary ki keys hai jismai maine list main value di hai. 
# Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.
import json


list1=["neelam","programmer","24","2400"] 
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
emp1={}
emp2={}
emp3={}
emp4={}
# dict1={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
list=[emp1,emp2,emp3,emp4]

for i in list1:
    emp1["name"]=list1[0]
    emp1["designation"]=list1[1]
    emp1["age"]=list1[2]
    emp1["salary"]= list1[3]

for i in list2:
    emp2["name"]=list2[0]
    emp2["designation"]=list2[1]
    emp2["age"]=list2[2]
    emp2["salary"]=list2[3]
 
for i in list3:
    emp3["name"]=list3[0]
    emp3["designation"]=list3[1]
    emp3["age"]=list3[2]
    emp3["salary"]=list3[3]

for i in list4:
    emp4["name"]=list4[0]
    emp4["designation"]=list4[1]
    emp4["age"]=list4[2]
    emp4["salary"]=list4[3]

out_file = open("question8.json", "w")

json.dump(list, out_file, indent = 2)

out_file.close() 




