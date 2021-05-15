import json
# text file
filename="text.txt"
# text will be store
dict={}
# creting dictinory
with open(filename) as fh:
    for line in fh:
        # read each line and tirms of extra the spaces
        # and gives only the velid words
        command, descripation=line.strip().split(None,1)
        dict[command]=descripation.strip()
# creating json file
out_file=open("ques7.json","w")
json.dump(dict,out_file,indent=4,sort_keys=True)
out_file.close()