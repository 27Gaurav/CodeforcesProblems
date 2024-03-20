n= int(input())
for t in range(n):
    m,k = map(int,input().split())
    l= list(map(int,input().split()))
    l1 = l[:m]
    l2 = l[m:]
 
    l1.sort()
    l2.sort()

    pl1 =[]
    pl2 =[]
    for i in range(m-1):
        if  l1[i]==l1[i+1]:
            
            pl1.append(l1[i])
            pl1.append(l1[i])
            l1[i]  = 0
            l1[i+1] = 0
        if l2[i]==l2[i+1]:
            pl2.append(l2[i])
            pl2.append(l2[i])
            l2[i]  = 0
            l2[i+1] = 0
    if 2*k<= len(pl1):
        p1 = pl1[:2*k]
        p2 = pl2 [:2*k]
        print(*p1,sep=" ")
        print(*p2, sep= " ")
    else:
        c= 2*k -  len(pl1)
        j=0
        while c!=0:
            if l1[j]!=0:
                pl1.append(l1[j])
                pl2.append(l1[j])
                j+=1
                c-=1
            else:
                j+=1
        print(*pl1,sep = " ")
        print(*pl2,sep= " ")







    