1. [find the smallest k element from an unsorted array of size n.](http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/)

```
Solution1: merge sort/quick sort O(n log n)
Solution2: maintain a maxheap of size k
1. heapify the first k-elements  O(k)
2. from the k+1 th element to the nth element for the current element X, if X<MAX-heap.top()  -> maxheap.pop() and then insert X;
else do nothing.
Time = O(k) + (n-k)log(k) 

Solution2: min heap
1. heapify the whole array O(n)
2. keep popping k times -> klog(n)
Time = O(n + klog(n))
其实是 O(c * n) + O(klog(n))

O(k) + (n-k)log(k)  vs  O(n + klog(n))
case(1)  k <<< n
	n log(k)       undecided      c * n
要看log(k) vs c谁更大
case(2)  k ~~~ n
	O(n) + O(nlogn)  	vs		O(nlogn)

Solution3: 
quick select

这个经典的例题，还要过一遍quick sort和四个方法都写熟练。 
```

动手实现一个heap有点难度，我不确定能不能handle





Quick Select

```python
def kthsmallest(lst, l, r, k):
  if k <= 0 or k > r - l + 1: return 'invalid'
  split_pos = partition(lst, l, r)
  
  if split_pos == k-1:
    return lst[split_pos]
  elif split_pos < k-1:
    return kthsmallest(lst, split_pos + 1, r, (k-1) - (split_pos - l))
  else:
    return kthsmallest(lst, l, split_pos - 1, k)

def partition(lst, start, end):
  pivot = lst[end]
  i = start - 1
  for j in range(start, end):
    if lst[j] <= pivot:
      i += 1
      lst[i], lst[j] = lst[j], lst[i]
  i += 1
  lst[end], lst[i] = lst[i], lst[end]
  return i
  
li = [1,2,3,4,5,6,7,8]
print(kthsmallest(li, 0, len(li)-1, 5))
```



Min-Heap

```python
import heapq

def kthsmallest(lst, k):
  return heapq.nsmallest(k, lst)[-1]

li = [0,1,2,3,4,5]
print(kthsmallest(li, 3))
```

