fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Error: File does not exist", fname)
    quit()

count = 0.0
spamconfidence = 0.0
for line in fh:

    if(line.startswith("X-DSPAM-Confidence:")):
        count = count + 1
        colonPos = line.find(":")
        value=float(line[colonPos+1:])
        spamconfidence = spamconfidence + value

print("Average spam confidence: ", spamconfidence/float(count))
