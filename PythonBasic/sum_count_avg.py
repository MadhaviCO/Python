sum=0
count=0;
while(True):
    num=input('Enter a number: (done with done)')
    if(num=='done'):
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    sum=sum + num
    count=count+1
if count==0:
    print("No numbers")
else:
    avg = float(sum) / float(count)
    print(sum,count,avg)
