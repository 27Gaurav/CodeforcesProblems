o=int(input())
for _ in range(o):
    n,m= map(int,input().split())
    a= list(map(int,input().split()))
    c= list(map(int,input().split()))
    l=[]
    for j in range(n):
        l.append([a[j],c[j]])
    l.sort()
    max_sum= 0
    for j in range(n):
        if j<n-1:
            if l[j+1][0]==l[j][0]+1:
                k1= min(l[j][1],m//l[j][0])
                k2 = min(l[j+1][1],(m-k1*l[j][0])//(l[j+1][0]))
                r= min(k1,l[j+1][1]-k2,m-k1*l[j][0]-k2*l[j+1][0])
                max_sum = max(max_sum,l[j][0]*(k1-r)+l[j+1][0]*(k2+r))
            else:
                k1= min(l[j][1],m//l[j][0])
                max_sum = max(max_sum,k1*l[j][0])
        else:
            k1= min(l[j][1],m//l[j][0])
            max_sum = max(max_sum,k1*l[j][0])

    print(max_sum)



                

        