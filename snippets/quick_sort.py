import random  # learn more: https://python.org/pypi/randompy

def quickSort(lst):
    quickSortHelper(lst, 0, len(lst) - 1)

def quickSortHelper(lst, start, end):
    if start < end:
        split_point = partition_diff(lst, start, end)

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
    rdm = random.randint(start, end)
    lst[rdm], lst[start] = lst[start], lst[rdm]
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
    l = [9, 8, 7, 6, 5, 4, 1, 1, 1, 1]
    quickSort(l)
    print(l)