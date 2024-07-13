n= int(input())
for i in range(n):
    m= int(input())
    la = list(map(int,input().split()))
    lb = list(map(int,input().split()))
    lc = list(map(int,input().split()))
    ans =[0]*6
    ver =False
    sum =0 
    for j in range(m):
        sum+= la[j]
        la[j] = sum
        
    sum = 0
    for j in range(m):
        sum+= lb[j]
        lb[j] = sum 
        
    
    sum = 0
    for j in range(m):
        sum+= lc[j]
        lc[j] = sum 
        

    def lif(n):
        if n==int(n):
            return int(n)
        else:
            return int(n)+1
    j=0
    v= 1
    ans[0]=(j+1)
   
    while j<m:
        if la[j]>=lif(sum/3):
            ans[1]=(j+1)
            break 
        else:
            j+=1
    
    t =j+1
    while t<m:
        if lb[t]-lb[j]>=lif(sum/3) :
            ans[2]= (j+2)
            ans[3] = t+1
            break 
        else:
            t+=1
    y= t+1
    while y<m:
        if lc[y]-lc[t]>=lif(sum/3) :
            ans[4]= (t+2)
            ans[5] = m
            break 
        else:
            y+=1
    if 0 not in ans:
        ver =True
    
    if ver and v:
        print(*ans, sep=" ")
        v=0
        ans =[0]*6
        
    elif not ver:
        ans =[0]*6
        j=0
        ans[0]=(j+1)
        while j<m:
            if la[j]>=lif(sum/3):
                ans[1]=(j+1)
                break 
            else:
                j+=1
        
        t =j+1
        while t<m:
            if lc[t]-lc[j]>=lif(sum/3) :
                ans[4]= (j+2)
                ans[5] = t+1
                break 
            else:
                t+=1
        y= t+1
        while y<m:
            if lb[y]-lb[t]>=lif(sum/3) :
                ans[2]= (t+2)
                ans[3] = m
                break 
            else:
                y+=1
    if 0 not in ans:
        ver =True
      
    if ver and v:
        print(*ans, sep=" ")
        v=0
        ans =[0]*6
    elif not ver:
        ans =[0]*6
        j=0
        ans[2]=(j+1)
        while j<m:
            if lb[j]>=lif(sum/3):
                ans[3]=(j+1)
                break 
            else:
                j+=1
        
        t =j+1
        while t<m:
            if la[t]-la[j]>=lif(sum/3) :
                ans[0]= (j+2)
                ans[1] = t+1
                break 
            else:
                t+=1
        y= t+1
        while y<m:
            if lc[y]-lc[t]>=lif(sum/3) :
                ans[4]= (t+2)
                ans[5] = m
                break 
            else:
                y+=1
    if 0 not in ans:
        ver =True
   
    if ver and v:
        print(*ans, sep=" ")
        v=0
        ans =[0]*6
    elif not ver:
        ans =[0]*6
        j=0
        ans[2]=(j+1)
        while j<m:
            if lb[j]>=lif(sum/3):
                ans[3]=(j+1)
                break 
            else:
                j+=1
        
        t =j+1
        while t<m:
            if lc[t]-lc[j]>=lif(sum/3) :
                ans[4]= (j+2)
                ans[5] = t+1
                break 
            else:
                t+=1
        y= t+1
        while y<m:
            if la[y]-la[t]>=lif(sum/3) :
                ans[0]= (t+2)
                ans[1] = m
                break 
            else:
                y+=1
    if 0 not in ans:
        ver =True
        
    if ver and v:
        print(*ans, sep=" ")
        v=0
        ans =[0]*6
    elif not ver:
        ans =[0]*6
        j=0
        ans[4]=(j+1)
        while j<m:
            if lc[j]>=lif(sum/3):
                ans[5]=(j+1)
                break 
            else:
                j+=1
        
        t =j+1
        while t<m:
            if lb[t]-lb[j]>=lif(sum/3) :
                ans[2]= (j+2)
                ans[3] = t+1
                break 
            else:
                t+=1
        y= t+1
        while y<m:
            if la[y]-la[t]>=lif(sum/3) :
                ans[0]= (t+2)
                ans[1] = m
                break 
            else:
                y+=1
    if 0 not in ans:
        ver =True
        
        
    if ver and v:
        print(*ans, sep=" ")
        v=0
        ans =[0]*6
    elif not ver:
        ans =[0]*6
        j=0
        ans[4]=(j+1)
        while j<m:
            if lc[j]>=lif(sum/3):
                ans[5]=(j+1)
                break 
            else:
                j+=1
        
        t =j+1
        while t<m:
            if la[t]-la[j]>=lif(sum/3) :
                ans[0]= (j+2)
                ans[1] = t+1
                break 
            else:
                t+=1
        y= t+1
        while y<m:
            if lb[y]-lb[t]>=lif(sum/3) :
                ans[2]= (t+2)
                ans[3] = m
                break 
            else:
                y+=1

    if 0 not in ans:
        ver =True
    if ver and v:
        print(*ans, sep=" ")
        v= 0
        ans =[0]*6
    elif not ver:
        print(-1)

            


    





