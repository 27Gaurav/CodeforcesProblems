n= int(input())
for j in range(n):
    m= int(input())
    tree = [0]*m
    for j in range(m-1):
        a,b= map(int,input().split())
        tree[a-1]+=1
        tree[b-1]+=1
    cnt= 0
    
    for j in range(m):
        if tree[j]==1:
            cnt+=1
    if cnt%2==0:
        print(cnt//2)
    else:
        print(cnt//2+1)


    