import re
fname = 'mbox-short.txt'
fh = open(fname)

count = 0
totalconfidence = 0.0
for line in fh:
    confidence = re.findall('^X-DSPAM-Confidence:\s+([0-9.]+)',line)
    if len(confidence)>0:
        totalconfidence = totalconfidence + float(confidence[0])
        count = count+1

print(totalconfidence, count)
