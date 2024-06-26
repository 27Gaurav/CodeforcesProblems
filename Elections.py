n= int(input())
for i in range(n):
    
    m,c= map(int,input().split())
    l= list(map(int,input().split()))
    high =max(max(l),l[0]+c)
    winner  =0
    for j in range(m):
        if l[j]== high and l[j]>l[0]+c:
            winner = j
            break 
    # print(winner)
    sum =[]
    s= 0
    for t in range(m):
        s+= l[t]
        sum.append(s)
    ans =[]
    for t in range(m):
        if t==winner:
            ans.append(0)
        else:
            if sum[t]+c >= high:
                ans.append(t)
            else:
                ans.append(t+1)
    print(*ans, sep=" ")

    