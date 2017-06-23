[71. Simplify Path](https://leetcode.com/problems/simplify-path/)

The key is to understand what we need [here](http://stackoverflow.com/questions/23242004/what-is-double-dot-and-single-dot-in-linux):

`.` represents the directory you are in and `..` represents the parent directory.

Use list comprehension and condition to sanitize input: We do not need `.` , `''` in our input. But we need `..` , as we need to take one level up in the path if we see this one.



```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_useful = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for p in path_useful:
            if p == "..":
                stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)
```

Time O(n) Sapce O(n)