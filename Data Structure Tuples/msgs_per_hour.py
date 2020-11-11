#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

fname = input('Enter name of the file(mbox-short.txt):')
try:
    fh = open(fname)
except:
    print("File does not exist")
    quit()

hours = dict()
for line in fh:
    words = line.split()
    if len(words)>2 and words[0] == "From":
        (hr,min,sec) = words[5].split(':')
        hours[hr] = hours.get(hr,0)+1

#print(hours)

hrList = hours.items()
#for k,v in hours.items():
    #hrList.append((k,v))

#hrList = hrList.sort(reverse=True)
#print(sorted(hrList,reverse=True))
for k,v in sorted(hrList):
    print(k,v)
