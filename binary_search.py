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

def binSearch_variant(a, target):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = start + (end - start) // 2
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if a[start] == target: return start
    return 'not found'

if __name__ == '__main__':
    a = [1]
    target = 4
    print(binSearch_variant(a, target))