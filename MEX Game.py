n= int(input())
for t in range(n):
    m =int(input())
    l= list(map(int,input().split()))
    l.sort()
    cnt =0
    if m ==1 :
        if l[0]==0:
            elm =1
        else:
            elm =0
    elif m>=1 :
        if l[0]<l[1]:
            cnt+=1
        ind = -1
        for i in range(1,m-1):
            if l[i-1]<l[i]<l[i+1]:
                cnt+=1
                if cnt ==2 :
                    ind = i
                    elm = l[i]
                    break
        
        if ind ==-1:
        
            if l[-1]> l[-2]:
                cnt +=1
                if cnt ==2 :
                    ind = m-1
                    elm = l[-1]
                else:
                    elm = l[ind]+1
            else:
                
                elm = l[ind] +1
    
        
        c= 0
        j=0
        while j<m:
            # if l[j]>=elm:
            #     break

            if l[j]==c:
                c+=1
            
                k =j+1
                while k<m:

                # for k in range(j,m):
                    if l[k]!=c-1:
                        j=k
                        break
                    else: 
                        k+=1
                        
            else:
                elm = min(c,elm)
                break
    print(elm)

    
