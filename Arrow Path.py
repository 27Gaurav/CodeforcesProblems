n= int(input())
for i in range(n):
    m= int(input())
    l1= str(input())
    l2 = str(input())
    l= [l1,l2]
    r= 1
    c= m-2
    ans ="YES"
    while c!= 0: 
        if l[r][c]!= '>':
            ans  = "NO"
            break
        else : 
            if c-2>=0:
                
                if l[r][c-2]=='>':
                    c-=2
                else :
                    if r ==1 :
                        if l[0][c-1] == '>':
                            c-=1
                            r=0
                        else :
                            ans = "NO"
                            break
                    else :
                        if l[1][c-1] == '>':
                            c-=1
                            r=1
                        else:
                            ans ="NO" 
                            break 
            else :
                break 
    print(ans)