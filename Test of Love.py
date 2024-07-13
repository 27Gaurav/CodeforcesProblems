o= int(input())
for i in range(o):
    n,m,k= map(int,input().split())
    l=str(input())
    cnt =0
    croc =0
    c1 =0
    ver =True
    for j in range(n):
        if l[j]=='W':
            cnt+=1
        elif l[j]=='C':
            cnt+=1
            c1 =cnt 
            croc=1
        else:
            # print(cnt)
            # print(c1)
            if croc:
                if m<=cnt:
                    if m<= c1:
                        ver =False
                        break
                    else:
                        k= k-(cnt-(m-1))
                        if k<0:
                            ver =False
                            break
            else:
                if m<=cnt:
                    k=k -(cnt-(m-1))
                    if k<0:
                        ver =False
                        break
            cnt =0
            croc =0 
    # print(cnt)
    if croc:
            if m<=cnt:
                if m<= c1:
                        ver =False
                        
                else:
                        k= k- (cnt-(m-1))
                        if k<0:
                            ver =False
                             
                    
    else:
                if m<=cnt:
                    k=k-(cnt-(m-1))
                    if k<0:
                        ver =False
    
    # print(c1)
    # print(cnt)
                        

    if ver :
        print("YES")
    else:
        print("NO")

    