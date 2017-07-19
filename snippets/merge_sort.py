def mergeSort(lst, start, end):
    if start < end:
        mid = start + (end - start) // 2
        mergeSort(lst, start, mid)
        mergeSort(lst, mid + 1, end)
        merge(lst, start, end, mid)


def merge(lst, start, end, mid):
    temp = lst[start: end + 1]
    left = 0
    right = mid + 1 - start
    index = start

    while left <= mid - start and right <= end - start:
        if temp[left] < temp[right]:
            lst[index] = temp[left]
            left += 1
        else:
            lst[index] = temp[right]
            right += 1
        index += 1

    # no need to copy right half since right half is already in the correct place
    while left <= mid - start:
        lst[index] = temp[left]
        index += 1
        left += 1

if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    mergeSort(l, 0, 4)
    print(l)

''' dummy merge sort, copy at first
def mergeSortMain(lst):
  temp = lst[:]
  mergeSort(lst, 0, len(lst) - 1, temp)

def mergeSort(lst, left, right, temp):
  if left < right:
    mid = left + (right - left) // 2

    mergeSort(lst, left, mid, temp)
    mergeSort(lst, mid + 1, right, temp)

    merge(lst, left, right, mid, temp)

def merge(lst, left, right, mid, temp):
    for i in range(left, right + 1):
      temp[i] = lst[i]
    left_index = left
    right_index = mid + 1
    while left_index <= mid and right_index <= right:
      if temp[left_index] < temp[right_index]:
        lst[left] = temp[left_index]
        left_index += 1
      else:
        lst[left] = temp[right_index]
        right_index += 1
      left += 1

    while left_index <= mid:
      lst[left] = temp[left_index]
      left += 1
      left_index += 1

l = [5,4,3,2,1]
mergeSortMain(l)
print(l)
'''

'''
Time O(n logn). logn levels, each level merge the n elements
Space O(n) extra Space
'''