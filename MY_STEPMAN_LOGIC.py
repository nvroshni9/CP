a=[int(i) for i in input().split(" ")]
L1=a[0]
S1=a[1]
L2=a[2]
S2=a[3]
i=1
j=0
flag=0
done=0
if (S1>0 and S2<0 and L1>L2) or (S1<0 and S2>0 and L1<L2):
    print("false")
elif(L1==L2):
    print("true")
elif(L1<L2 and S1<L1-L2):
    print("false")
else:
    while(i<=1000):
        if L1+i*S1==L2+j*S2:
            print("true")
            done=1
            break
        if(flag==0):
            j+=1
            flag=1
        else:
            i+=1
            flag=0
    if (done==0):
        print("false")
