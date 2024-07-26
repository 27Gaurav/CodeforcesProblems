n= int(input())
for o in range(n):
    m,d= map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    i=0
    j=0
    k=0
    sumik=0
    sumkj=0 
    max_sum=0 
    while j<m:
        if l[j]==l[k]:
            sumkj+=l[j]
            if sumik+sumkj<=d:
                max_sum= max(max_sum,sumik+sumkj)
            else:
                while i<k:
                    sumik-=l[i]
                    i+=1
                    if sumik+sumkj<=d:
                        max_sum= max(max_sum,sumik+sumkj)
                        break 

            j+=1
        else:
            
            
            if l[j]-l[k]==1:
                i=k
                k=j
                sumik=sumkj 
                sumkj=0
            else:
                k=j
                i=k
                sumik= 0
                sumkj=0 
    # max_sum= max(max_sum,sumik+sumkj)
    print(min(max_sum,d))


                


