n= int(input())
for i in range(n):
    
    m,k= map(int,input().split())
    if (m-1)%2==0:
        max =  ((m-1)*(m-1+2))//2 
    else:
        max = (m*m)//2
    # print(max)
    if k%2 != 0:
        print("NO")
    elif k>max :
        print("NO")
    else:
        j= 0
        l= [0]*m
        # l1 =l
        print("YES")
        k =k//2
        # print(m)
        # print(k)
        while k>m-1:
            l[j+m-1] = j+1
            l[j] =j+m-1 +1
            # l[m-1] = j+1
             
            k-= m-1
            m-=2
            j+=1
            # l1= l[j:m] 
        
        # print(l1)
        # print(l)
        # print(k)
        if k!=0 :
            l[j+k] = j+1
            l[j] = k+1+j
        # print(l1)
        # print(l)
        for t in range(len(l)):
            if l[t]== 0:
                l[t]= t+1 
        # print(l)
        print(*l,sep=" ")


            


    
