#input the names, and determine which name is most common
#using dictionaries

names = dict()
while True:
	name = input("Enter a name: ")
	if name == "done":
		break
	names[name] = names.get(name, 0) + 1

	#if name in names:
	#	names[name] += 1
	#else:
	#	names[name] = 1

max = 0
maxName = ""
for name in names:
	if names[name] > max:
		 max = names[name]
		 maxName = name

print(maxName,"is most common")
