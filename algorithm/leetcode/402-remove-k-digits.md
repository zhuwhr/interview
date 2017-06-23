[402-remove-k-digits](https://leetcode.com/problems/remove-k-digits/#/description)

```python
idea: 
    1. find all pairs that num[i] > num[i+1], remove digit i and decreasing k
    2. if k is still not zero, meaning the result is increasing, then remove the last k digits.
    3. strip the leftmost 0s in the result
    4. return 0 if the result is an empty array.
    key points:
    Remove only when is larger the succeding, then remove the last k digits if k
    fancy:
    The problem is too many corner cases to consider. This solution handle them together from two parts: 1.strip leading 0s. 2. return 0 if result is an empty string
    class Solution(object):
        def removeKdigits(self, num, k):
            """
            :type num: str
            :type k: int
            :rtype: str
            """
            stack = []
            for c in num:
                while stack and stack[-1] > c and k:
                    k -= 1
                    stack.pop()
                stack.append(c)
            
            return ''.join(stack[:-k or None]).lstrip('0') or '0'
    # Time: O(n) constant on each digit
    # Space: O(n) stack and it's shallow copy    
    
    '''自己写出来的，虽然很闪耀，但还是一坨垃圾
    if len(num) == k: return '0'
    if num[k] == '0':
        return str(int(num[k:]))
    
    stack = []
    for c in num:
        while stack and stack[-1] > c and k > 0:
            k -= 1
            stack.pop()
        stack.append(c)
    
    idx = 0
    while stack[idx] == '0':
        idx += 1
    stack = stack[idx:]
        
    return ''.join(stack[:-k]) if k > 0 else ''.join(stack)
    '''
```