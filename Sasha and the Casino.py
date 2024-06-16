n= int(input())
for i in range(n):
    k,x,a = map(int,input().split())
    d =a
    ver =True
    for i in range(x):
        if (a+1-d)/(k-1)== (a+1-d)//(k-1):
            m = ((a+1-d)//(k-1))
        else:
            m = ((a+1-d)//(k-1)) +1 
        if m<=d :
            d-=m 
        else:
            ver =False 
            break
    if ver :
        if d*(k)>=a+1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

        