[78. Subsets](https://leetcode.com/problems/subsets/)

Idea: Recursion Tree.

- each level decides whether to add current element or not
- each node has two children: either add or not

```python
# S0
class Solution(object):
    def subsets(self, nums):
        def dfs(nums, index, subset):
            if index == len(nums):
                res.append(subset)
                return
            dfs(nums, index+1, subset+[nums[index]])
            dfs(nums, index+1, subset)
        
        res = []
        dfs(nums, 0, [])
        return res
# S1
class Solution(object):
    def subsets(self, nums):
        def dfs(nums, index, subset):
            if index == len(nums):
                res.append(list(subset))
                return
            subset.append(nums[index])
            dfs(nums, index+1, subset)
            subset.pop()
            dfs(nums, index+1, subset)
        
        res = []
        dfs(nums, 0, [])
        return res
# S2
class Solution(object):
    def subsets(self, nums):
        # 递归的定义：在 Nums 中找到所有以 subset 开头的的集合，并放到 results
        def dfs(nums, index, subset):
            res.append(list(subset))
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs(nums, i+1, subset)
                subset.pop()
        
        res = []
        # nums.sort() 没有重复时，不需要排序
        dfs(nums, 0, [])
        return res
```

Analysis:

Time O(2^n), n elements mean n level on recursion tree, each element has two conditions.

为什么S1比S0要好：

S0中，`subset + [nums[level]]` 这个操作是创建了一个新的对象（`+` 操作会创建一个新的对象，而list.append()不会，只是对原有的对象进行了修改），也就是说每次递归时都会创建一个新的对象。而S1中，只有subset一个对象，每次递归时只是传一个reference，当需要存储的时候，才copy，比S0的写法要省空间。

S2和S1/S0的思路有什么区别：

递归树每层代表的意义不同。S2中，每层代表的是结果中的position，一共有position层，如(a,b,c)就是有三层。节点的值就是这个位置放哪个元素，选元素的时候只能按照原数组中的index往后选，不能往前选，这样避免了重复。在这棵树中，每个节点的值都应该被加到最后的结果中，复杂度就是O(2^n)。

而S0/S1中，每层代表的是对于当前元素，是否使用这个元素。这棵树一共有元素个数的层数，层数上和上面那棵树一样。这棵树的最下面一层才是我们想要的结果，最下面一层的复杂度是O(2^n)，实际复杂度是(1+2^1+2^2+...+2^n)，量级一样，实际上大一点。但是这种方法的好处是思路比较清晰，容易扩展到其他问题上。选用哪种取向看个人思维习惯。

```
set = {a, b, c}
# S0/S1
			None
		/			\
a:		a			None
	 /		\		/	  \
b:   ab		a		b		None
	/  \   /  \    /   \   /    \
c: abc  ab ac  a  bc   b   c    None

# S2
				    None
			/  		  |			\
pos0		a		  b			c
		  /	  \		  |		
pos1	 ab   ac      bc
		  |
pos2	 abc
```



Bugs

1. Only at the last level, should we add the subset to final solution. `index == len(nums)`. Otherwise, we will have duplicates.

2. When adding a reference to a solution, if the reference is mutable and is changed somewhere in the method, be sure to add a copy of it, otherwise  the reference maybe changed and the final solution may not contain what we want.

   See S1 line 19, we add a copy of subset, as the array that subset refers to is changed in the dfs method. If we don't add the copy, we will add all empty array to the final solution. Because we add multiple subset reference to the result, and the subset refers to an empty array in the end, so all arrays in the result would be empty.

   Another way to do it is S0: we don't change the reference of subset, instead, we change the argument of each recursive call. Each dfs call, we have a new reference of subset. So we do not need to make a copy of it.

   S0的写法中，只有一个subset reference，这个reference是在不断地变化的。在S1中，每次传参的时候传的是`subset + [nums[index]]`，相当于在下一层函数调用时，赋予形参一个值：`subset = subset + [nums[index]]` ，创造了一个新的subset reference。每层递归函数中都有自己的作用域，所以这些名称相同的subset reference并不冲突，最终结果里保存的，虽然也都是reference，但是这些reference的指向并不同，所以结果是对的。