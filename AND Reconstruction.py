n= int(input())
for  i in range(n):
    m= int(input())
    l=list(map(int,input().split()))
    ans =[] 
    ans.append(l[0])
    ver =True
    for j in range(m-2):
        ans.append(l[j] | l[j+1] )
        if ans[-1] & ans[-2] != l[j]:
            ver =False
            break
    ans.append(l[-1])
    if ans[-1] & ans[-2] != l[-1]:
        ver =False
    if ver:
        print(*ans, sep=" ")
    else:
        print(-1)
     