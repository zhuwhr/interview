'''
abcdefg1234567  ->  a1b2c3d4e5f6g7
KEY: even odd manipulation
'''

def shuffle(lst, left, right):
    if right - left <= 1: 
        return
    length = right - left + 1
    mid = left + length // 2
    # cal mid for left and right
    left_mid = left + length // 4
    right_mid = left + length * 3 // 4

    reverse(lst, left_mid, mid - 1)
    reverse(lst, mid, right_mid - 1)
    reverse(lst, left_mid, right_mid - 1)

    # select the correct boundary
    shuffle(lst, left, left + 2 * (left_mid - left) - 1)
    shuffle(lst, left + 2 * (left_mid - left), right)

def reverse(lst, left, right):
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
if __name__ == '__main__':
    s = 'abcdefg1234567'
    lst = list(s)
    shuffle(lst, 0, len(s) - 1)
    res = ''.join([str(e) for e in lst])
    print(res)
