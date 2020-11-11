# find the most common word from a File

fname = input("Enter Filename: ")
try:
    fh = open(fname,"r")
except:
    print("File does not exist: ", fname)
    quit()

allWords = dict()
for line in fh:
    wordsInTheLine = line.split()
    for word in wordsInTheLine:
        allWords[word] = allWords.get(word,0) + 1

maxCount = None
commonWord = None

for word,count in allWords.items():
    if maxCount is None or count > maxCount:
        commonWord = word
        maxCount = count
#for word in allWords:
#    if allWords[word] > maxCount:
#        maxCount = allWords[word]
#        commonWord = word

print(allWords)
print("\nMost common word", commonWord,"Occurred",maxCount,"Times\n\n")
