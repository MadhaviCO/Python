#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the most number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter File Name: ")
try:
    fh = open(fname, "r")
except:
    print("Error, file does not exist", fname)
    quit()

senders = dict()
#print("\n\n-----------------------\n\n")
for line in fh:
    if len(line) > 1:
        words = line.split()
        #print(words)
        if len(words) > 2 and words[0] == "From":
            print(words)
            senders[words[1]] = senders.get(words[1],0) + 1

maxcount = None
commonSender = None
print("\n\n-----------------------\n\n")
for sender,count in senders.items():
    #print(sender, count)
    if maxcount is None or count > maxcount:
        maxcount = count
        commonSender = sender

#print("\n\n-----------------------\n\n")
print(commonSender, maxcount)
