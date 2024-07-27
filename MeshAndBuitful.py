def min_swap(p):
    n = len(p)
    def merge_sort(l, r):
        if l == r:
            return 0
        mid = (l + r) // 2
        left_swaps = merge_sort(l, mid)
        right_swaps = merge_sort(mid + 1, r)

        if left_swaps == -1 or right_swaps == -1:
            return -1
        
        left_half = p[l:mid+1]
        right_half = p[mid+1:r+1]
        
        if left_half == sorted(left_half) and right_half == sorted(right_half):
            if left_half[-1] <= right_half[0]:
                return left_swaps + right_swaps
            elif right_half[-1] <= left_half[0]:
                return left_swaps + right_swaps + 1
        return -1
    
    return merge_sort(0, n - 1)

t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    result = min_swap(p)
    print(result)
