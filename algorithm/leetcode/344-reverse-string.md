[344-reverse-string](https://leetcode.com/problems/reverse-string/#/description)

Idea: we can use two pointer, one start from beginning and one start from the end. Swap the element at the two indices, until the left one `>=` the right one.

In python, we have a couple of tricks:
1. [extended slice](https://docs.python.org/2/whatsnew/2.3.html#extended-slices)
   the solution is simple: `return s[::-1]`
   Notice that the format of extended slice  `s[start:end:step]`. The step parameter: default is +1. The sign  indicates forward or backward, absolute value of step indicates steps. Default is forward with step size 1. Positive means forward, negative means backward. This is why `s[::-1]` can start from the end.
   Also notice that, string in python is **immutable**. Using slice only returns a copy of original string and it does not change the value of the string. We can not assign a value like this `s[1] = 'a'`.

2. Reverse as a list
        ```
        s1 = list(s)
        s1.reverse()
        return ''.join(s1)
       		```
   s1 is a list generated by list() constructor. The elements are chars in the original string s. When calling reverse(), it returns an iterator that holds the element in the list in a reversed order. `join` is a method of strings. That method takes any iterable and iterates over it and joins the contents together. (The contents have to be strings, or it will raise an exception.)
   ​			