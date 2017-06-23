[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)



Idea: sanitize the input string, excape all the `:, . ` etc. and only keep the letters and numbers.

Trick:

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_char_list = [i.lower() for i in s if i.isalnum()]
        return new_char_list == new_char_list[::-1]
```



Two pointers:

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
```

