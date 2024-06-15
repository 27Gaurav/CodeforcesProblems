n= int(input())
for t in range(n):
    m= int(input())
    req = 0 
    rem = m%30 
    div =m//30
    l= [0,1,2,1,2,3,1,2,3,2,1,2,2,2,3,1,2,3,2,3,2,2,3,3,3,2,3,3,3,4,2]
    # print(len(l))
    def coin(m):
        return l[m]
    
        
    if div!=0:
        if rem<15 :
            req = min((m//30)*2  + coin(m%30) , (m//30)*2 -1 + coin(m%30 + 15))
        else :
            req = div*2 + coin(rem)
    else:
        req += (m//30)*2
        req+= coin(rem)

    print(req)