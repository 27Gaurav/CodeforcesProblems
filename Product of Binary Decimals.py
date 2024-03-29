n= int(input())
# l =[10,1111,1001,1011,1101,111,101,11]
l= [10,11,101,111,1101,1011,1001,1111]
for i in range(n):
    m= int(input())
    s= str(m)
    ver =True
    for k in range(len(s)):
        if s[k] != '0' and s[k]!='1' :
            ver =False 
            break 
    if ver : 
        print("YES")
    else:
        if m==1 :
            print("YES")
        
        else :
            while m!= 1 :
                t= m
                for j in range(len(l)):
                    if t%l[j]==0:
                        t=t//l[j]
 
                if t==m: 
                    print("NO")
                    break 
                else : 
                    m= t 
            if m==1:
                print("YES")