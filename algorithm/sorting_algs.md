## MergeSort

Divide and conquer, comparison based algorithm. It runs in O(n lgn) time with O(n) space.

It divides the array into two half, make a copy and recursively call merge sort on each half. Then we have two sorted half, and merge it. When merging, we put the smaller element back to the original array. After one side is done, we put the other side to the rest of the original array.

```python
def mergeSort(lst):
  if len(lst) > 1:
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    mergeSort(left_half)
    mergeSort(right_half)
    
    # merge 
    left, right, index = 0,0,0
    while left < len(left_half) and right < len(right_half):
      if left_half[left] < right_half[right]:
        lst[index] = left_half[left]
        left += 1
      else:
        lst[index] = right_half[right]
        right += 1
      index += 1
    
    while left < len(left_half):
      lst[index] = left_half[left]
      index += 1
      left += 1
    
    while right < len(right_half):
      lst[index] = right_half[right]
      right += 1
      index += 1

'''
Time O(n logn). logn levels, each level merge the n elements
Space O(n) extra Space
'''
```

## Quick Sort

It runs in O(n lgn) on average, with in place operation.

High-level: first it picks a pivot, compare every elem with the pivot, put the smaller elements on one side of the pivot, and the larger one on the other side. There are several ways of how to compare with the pivot: Move the cursor in the same direction(CLRS) or in different directions (from both sides). 

I follow the CLRS and move the cursor from the same direction. First pick a pivot and swap it to the end of the array, then make two cursors. Smaller from `start -1`, larger from `start`. Anytime find an elem larger, just move the larger cursor. Anytime find an smaller elem, increase smaller cursor, swap with the larger cursor(swap a larger one to a smaller one), then move the cursor.

Also, we can pick up a cursor in anyway, first, last or mid element. Here we use a randomized way of picking a pivot, and swap it to the last. 

```python
import random # learn more: https://python.org/pypi/randompy
def quickSort(lst):
  quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, start, end):
  if start < end:
    split_point = partition_same(lst, start, end)
    
    quickSortHelper(lst, start, split_point - 1)
    quickSortHelper(lst, split_point + 1, end)

# move cursor from same direction (CLRS) 
def partition_same(lst, start, end):
  # randomnized choosing pivot
  rdm = random.randint(start, end)
  lst[rdm], lst[end] = lst[end], lst[rdm]
  pivot = lst[end]
  smaller = start - 1
  for larger in range(start, end):
    if lst[larger] <= pivot:
      smaller += 1
      lst[smaller], lst[larger] = lst[larger], lst[smaller]
  smaller += 1
  lst[smaller], lst[end] = lst[end], lst[smaller]
  return smaller

# move cursor from start and end (online) 
def partition_diff(lst, start, end):
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
```

Analysis:

Worst case: O(n ^ 2). Each time picking up a pivot, it does not split the array at all, meaning the final position of the pivot is at the start/end of the array. `T(n) = T(n-1) + T(0) + O(n)`

Best case: O(n lgn). Each time picking up a pivot, it splits the array just at the half. `T(n) = 2T(n/2) + O(n)`

Average case: O(n lgn). It does not matter how much we split the array. The recursion tree level would be in O(lgn), and in each level is O(n)

There are also intuitive proof and precise proof by indicator variable in CLRS. Refer it when necessary.