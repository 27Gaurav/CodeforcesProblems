n= int(input())
for t in range(n):
    m= int(input())
    s1 =str(input())
    s2 =str(input())
    l= [s1[0]]
    i= 1
    # j= 0
    check =True
    ways =1
    while i<m:
        if check: # we are in upper array 
            if s1[i]<=s2[i-1]:
                if s1[i]<s2[i-1]:
                    l.append(s1[i])
                    i+=1
                    # j+=1
                else:
                    way =0
                    for t in range(i,m):
                        if s1[t]<s2[t-1]:
                            l.append(s1[t])
                            way =0
                            break
                        elif s1[t]> s2[t-1] :
                            l.append(s2[t-1])
                            
                            check =False
                            break
                        else:
                            way+=1
                            l.append(s1[t])
                    ways+=way
                    i = t+1
                      

                        
            else:
                check =False
                l.append(s2[i-1])
                i+=1
                # j+=1
        else: #we are in lower array
            l.append(s2[i-1])
            # j+=1
            i+=1
    l.append(s2[m-1])
    print(*l,sep="")
    print(ways)