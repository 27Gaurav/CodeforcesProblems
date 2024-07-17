n= int(input())
for i in range(n):
    m= int(input())
    s=list(input())
    l=[]
    l1=[]
    ver =True
    j=0
    while j<m-1:
        if s[j]>s[j+1]:
            l.append(s[j])
            l1.append(j)
            if len(l)>1:
                if l[-1]>l[-2]:
                    ver=False
                    break 
            j+=1
        elif s[j]==s[j+1]:
            # cnt=1
            t= j+1
            while t<m-1:
                if s[t]!=s[j]:
                    break
                else:
                    t+=1
            
            
            if s[j]>=s[t]:
                if l:
                    if s[j]>l[-1]:
                        ver=False
                        break
                
                cnt = t-j
                for d in range(cnt):
                    l.append(s[j])
                    l1.append(j+d)
            j=t
        else:
            j+=1
    if l:
        if s[m-1]>l[-1]:
            ver= False
    l.append(s[m-1])
    l1.append(m-1)
    # print(l)
    
    for t in range(len(l1)):
        s[l1[t]]=l[-1-t]
    for j in range(m-1):
        if s[j]>s[j+1]:
            ver=False
            break
    j=0
    while j<len(l):
        if l[j]!=l[0]:
            break
        j+=1
    if ver:
        
            
        print(len(l)-j)
    else:
        print(-1)
    
            
        




    