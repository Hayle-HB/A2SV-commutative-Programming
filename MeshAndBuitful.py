t = int(input())

for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    
    swaps = 0
    possible = True
    
    stack = [(0, m - 1)]
    
    while stack and possible:
        left, right = stack.pop()
        
        if left < right:
            mid = left + (right - left) // 2
            stack.append((left, mid))
            stack.append((mid + 1, right))
        else:
            if left == right:
                continue
            
            mid = left + (right - left) // 2
            if p[left] > p[right]:
                p[left:mid+1], p[mid+1:right+1] = p[mid+1:right+1], p[left:mid+1]
                swaps += 1
                
            elif p[mid] > p[mid + 1]:
                possible = False
    
    if possible:
        print(swaps)
    else:
        print(-1)
