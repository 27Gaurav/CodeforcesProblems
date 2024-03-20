n= int(input())
for i in range(n):
    m= int(input())
    l =list(map(int,input().split()))
    # for j in range(m):
    #     l[j] =[l[j],j]
    # l.sort()
    l1 =[m]*m
    # j=0
    # cnt=0
    # while j<m:
    #     for k in range(j+1,m):
    #         if l[k]==l[j]:
    #             cnt+=1
    #             l1[k]=cnt
    #         else:
    #             j=k
    #             brea
    j=0
    k=1
    while k<m:
        if l[k]!=l[j]:
            for f in range(j,k):
                l1[f]=k
            j=k
            k+=1
        else:
            k+=1
        
        


   
    q =int(input())
    for t in range(q):
        a,b =map(int,input().split())
        if l1[a-1]<=b-1:
            ans=[a,l1[a-1]+1]
            
        else:
            ans=[-1,-1]
        print(*ans,sep=" ") 


        
    
