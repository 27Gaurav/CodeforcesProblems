import sys
t = int(input())
for _ in range(t):
        n = int(input())
        ans = []
        
        for i in range(2, n + 1):
            prev = 1
            while True:
                print(f"? {i} {prev}")
                sys.stdout.flush()
                
                x = int(input().strip())
                if x == i:
                    break
                prev = x
            
            ans.append((i, prev))
        
        print("! ", end="")
        for x in ans:
            print(f"{x[0]} {x[1]} ", end="")
        print()
        sys.stdout.flush()
