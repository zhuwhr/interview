'''
http://www.geeksforgeeks.org/counting-inversions/
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''

# idea: merge sort, on merging, when take right, count += len(left)
def count_inversion(arr):
  # input: array of integer
  # output: int, count of inversions
    count = [0]
    def count_helper(arr, start, end):
        if start < end:
            mid = start + (end - start) // 2
            count_helper(arr, start, mid)
            count_helper(arr, mid + 1, end)
            merge(arr, start, end, mid)

    def merge(arr, start, end, mid):
        temp = arr[start : end + 1]
        left = 0
        right = mid + 1 - start
        index = start
        while left <= mid - start and right <= end - start:
            if temp[right] < temp[left]:
                arr[index] = temp[right]
                index += 1
                right += 1
                count[0] += mid + 1 - left
            else:
                arr[index] = temp[left]
                left += 1
                index += 1
        while left <= mid - start:
            arr[index] = temp[left]
            left += 1
            index += 1
    count_helper(arr, 0, len(arr) - 1)
    return count[0]

if __name__ == '__main__':
    arr = [2,4,1,3,5]
    print(count_inversion(arr))