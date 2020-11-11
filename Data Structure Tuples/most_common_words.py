#find the top 10 most common words from a File
fname = input("Enter name of the file: ")
if len(fname) < 1 : fname = "clown.txt"
try:
    fh = open(fname)
except:
    print("File does not exist!")
    quit()

wcounts = dict()
for line in fh:
    words = line.split()
    for word in words:
        wcounts[word] = wcounts.get(word,0) + 1

#print(wcounts)

wcountlist = list()
for k,v in wcounts.items():
    wcountlist.append((v,k))

wcountlist = sorted(wcountlist, reverse=True)

for (v,k) in wcountlist[:10]:
    print(k,v)
