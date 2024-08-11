exec(open('util.py').read())
#exec(open('test.py').read())

file_name = "earn_aug_19" #without extension
text = load_data([file_name+".txt"])


text =text.replace("\n\n","\n")
values = nex4([text,"\n","\n"])
for a,val in enumerate(values):
    values[a] = val.replace("\n","")
values2 = []
for a,val in enumerate(values):
    if len(val)>5:
        continue
    if len(val)==0:
        continue
    
    if [val] not in values2:
        values2.append([val])
values = values2
pri(values)
write_data([file_name+".xls",values])  
