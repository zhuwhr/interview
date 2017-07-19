# find the kth smallest element in an array

def quickSelect(lst, left, right, k):
    if k > right - left + 1 or k < 0: return 'not found'
    pos = partition(lst, left, right)

    if pos - left == k - 1:
        return lst[pos]
    elif pos - left > k - 1:
        return quickSelect(lst, left, pos-1, k)
    else:
        return quickSelect(lst, pos + 1, right, k - pos + left - 1)

    return 'not found'

def partition(lst, start, end):
    pivot = lst[start]
    left = start + 1
    right = end
    while left <= right:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and lst[right] >= pivot:
            right -= 1
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
    lst[start], lst[right] = lst[right], lst[start]
    return right


if __name__ == '__main__':
    lst = [3,5,1,6,2,8]
    print(quickSelect(lst, 0, len(lst)-1, 5))

'''
O(n) time. Proof is complex, but intuitively, 
each time we only select one half of the array. The total size would be:
n + n/2 + n/4 + n/8 +... < 2n
this is evenly partition case(best case), the average case would be unevenly partition,
which is the same as best case. Proof is in CLRS quick sort part.
'''