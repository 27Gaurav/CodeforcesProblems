n= int(input())
for i in range(n):
    m= int(input())
    l=list(map(int,input().split()))
    ans =[]
    for j in range(40):
        num = (min(l)+max(l))//2
        if num==0:
            break 
        for t in range(m):
            l[t] =abs(l[t]-num)
        ans.append(num)
    if l==[0]*m:
        print(len(ans))
        print(*ans,sep=" ")
    else:
        print(-1)
