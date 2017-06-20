def binSearch(a, target):
    start = 0
    end = len(a) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            start = mid
        else:
            end = mid

    if a[start] == target: return start
    if a[end] == target: return end

    return 'not finding'

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 4
    print(binSearch(a, target))