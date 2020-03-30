lst_pairs = []
'''
with open('file.txt','r') as fp:
    lines = f.readlines()
    fp.close()
'''
lines = ["1:3","abc:def"]
for i in lines:
    # each line contains an entry of two strings, separated by a :
    # e.g. check:true
    lst_pairs.append(i.split(":"))

# Find unique set of entries
uq_pairs = set(lst_pairs)
     