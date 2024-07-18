o= int(input())
for i in range(o):
    n= int(input())
    s=str(input())
    t= str(input())
    ver=True
    for j in range(n):
        if s[j]=='0' and t[j]=='1':
            ver =False
            break 
        if s[j]=='1':
           
            break 
    if ver:
        print("YES")
    else:
        print("NO")
    
