[541-reverse-string-ii](https://leetcode.com/problems/reverse-string-ii/#/description)

idea: iterate the input string by 2k block. Handle the corner case then.

original solution:
```python
        i = 0
        l = list(s)
        while i + 2 * k <= len(s):
            l[i:i+k] = reversed(l[i:i+k])
            i += 2 * k
        if i + 2 * k > len(s) and i + k <= len(s):
            l[i:i+k] = reversed(l[i:i+k])
            return "".join(l)
        else:
            l[i:len(s)] = reversed(l[i:len(s)])
            return "".join(l)
```

optimized solution:
```python
	def reverseStr(self, s, k):
      s = list(s)
      for i in range(0, len(s), 2*k):
          s[i:i+k] = reversed(s[i:i+k])
      return "".join(s)
```


To Notice:
1. `reversed` is a builtin function: return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
2. list.reverse(). Reverse the elements of the list in place, but it can not work with slice like this `list(range(10))[0:2].reverse`
3. `range()` builtin function: The full form returns a list of plain integers [start, start + step, start + 2 * step, ...]. If step is positive, the last element is the largest start + i * step less than stop; if step is negative, the last element is the smallest start + i * step greater than stop. step must not be zero (or else ValueError is raised). 


Stupid bugs:
1. 难以想像，我一开始就写了一个if循环，像这样：脑子被门夹了吗。什么时候用while和if都分不清了，对着返回的null愣了半天，想啥呢这是。最后一个一个加断点发现没有进到elif里去才反应过来。
        i = 0
        l = list(s)
        if i + 2 * k <= len(s):
            l[i:i+k] = reversed(l[i:i+k])
            i += 2 * k
        elif i + 2 * k > len(s) and i + k <= len(s):
            l[i:i+k] = reversed(l[i:i+k])
            return "".join(l)
        else:
            l[i:len(s)] = reversed(l[i:len(s)])
            return "".join(l)

2. 最后一个corner case `l[i:-1]` 这样没有算上最后一个元素，少年，是要出bug的！