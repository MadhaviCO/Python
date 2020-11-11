fh=open("romeo.txt","r")
count=0
for line in fh:
	print(line.strip())
	count = count+1

print(count,"Lines")
fread = fh.read()
print("Characters", len(fread))
