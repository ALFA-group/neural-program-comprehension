lst_pairs = []

with open('file.txt','r') as fp:
    lines = fp.readlines()
    fp.close()

for i in lines:
# each line has two strings,
# separated by a colon (:)
# e.g. check:true
    lst_pairs.append(i.split(":"))

# Find unique set of entries
uq_pairs = set(lst_pairs)
