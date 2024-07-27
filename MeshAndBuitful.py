def merge_sort(left, right):
    if left < right:
        mid = left + (right - left)//2
        l = merge_sort(left, mid)
        r = merge_sort(mid+1, right)
        if l and r:
            return merge(left, mid, right)
        return False
    return True

def merge(left, mid, right):
    
    if num[left] > num[right]:
        num[left:mid+1],num[mid+1:right+1] = num[mid+1:right+1],num[left:mid+1]
        swaps[0] += 1
        return True
    elif num[mid] < num[mid+1]:
        return True
    
    return False

t = int(input())

while t > 0:
    m = int(input())
    num = list(map(int, input().split()))

    swaps = [0]
    if merge_sort(0, m-1):
        print(swaps[0])
    else:
        print(-1)

    t -= 1
