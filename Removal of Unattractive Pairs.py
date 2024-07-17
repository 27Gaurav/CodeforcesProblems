n= int(input())
for j in range(n):
    m=int(input())
    s=str(input())
    maxi= 0
    l=[0]*26
    for j in range(m):
        l[ord(s[j])-97]+=1
    maxi =max(l)
    if 2*maxi-m<=0:
        if m%2==0:
            print(0)
        else:
            print(1)
    else:
        print(2*maxi-m)