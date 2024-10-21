n= int(input())
m= 0 
for t in range(n) :
    m= int(input())
    l= list(map(int,input().split()))
    if l[0]<10:
        last = l[0]
    else :
        s= str(l[0])
        
        if int(s[0])<=int(s[1]):
 
            last = int(s[1])
        else:
            last = l[0]
    ans ="YES"
    for i in range(1,m):
        if l[i]<10:
            if l[i]>= last :
                last = l[i]
            else: 
                ans = "NO"
                break
        else : 
            i1 = int(str(l[i])[0])
            i2 = int(str(l[i])[1])
        
            if i1<=i2 :
                if i1>= last:      
                    last = i2
                else: 
                    if l[i]>= last :
                        last = l[i]
                    else:
                        ans = "NO"
                        break
 
            else:
                if l[i]>=last :
                    last = l[i]
                else:
                     ans = "NO"
                     break
    print(ans)
 
            
