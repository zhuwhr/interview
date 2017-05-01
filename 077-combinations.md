[77. Combinations](https://leetcode.com/problems/combinations/)

Idea1: Standard Backtracking

Use a level to track the number of elements, when level reaches k, it means that is has k element in each solution. This approach takes O(n!) time, as standard backtrack does. But leetcode makes strict test cases. This one got TLE. I am not sure how to modify backtrack though.

```python
# 返回以combination为开头的所有合法解
def combine(n, k):
  def dfs(n, index, level, combination):
      if level == k:
          res.append(list(combination))
          return
      for i in range(index, n+1):
          combination.append(i)
          dfs(n, i+1, level+1, combination)
          combination.pop()
  res = []
  dfs(n, 1, 0, [])
  return res
```

Idea2: C(n, k) = C(n-1, k-1) + C(n-1, k)

A little math here. One situation is that we do not select n, so we select k numbers from the rest n-1, another is that we select n, so we select k-1 numbers from the reset n-1 and append n for each solution. This one is AC.

```python
    def combine(self, n, k):
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            res=[]
            #n is not selected
            res += self.combine(n-1,k)
            #n is selected
            temp = self.combine(n-1,k-1)
            for lst in temp:
                lst.append(n)
            res += temp
            return res
```

Analysis: I am not sure here. Looks O(n!) to me.

### 