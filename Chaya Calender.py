n= int(input())
for i in range(n) : 
    m= int(input())
    l= list(map(int,input().split()))
    t= l[0]
    for i in range(1,m):
        if l[i]>t :
                t= l[i]
        else :
            t= l[i] * (t//l[i]) + l[i]
        
    print(t)
            
