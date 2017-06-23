[90. Subsets II](https://leetcode.com/problems/subsets-ii/)

Key point: How to skip the duplicated elements.

First we need to sort the set to make the duplications together. Since all duplications are the same, we need a way to skip the rest of them when we use them once.

In S1, the level in recursion tree means elements and whether we add the element in this level. When add, need no change. When not add, then we need to choose the next **different** element to decide whether to add or not. Because if we choose the duplicated elements, and we decide to add, then it will have duplications in the final results (dup with the one that in last level we choose add and this level choose not).

In S2, the level in recursion tree means position in final results. When add the next element to this position, we need to make sure that the element we are going to add is different with the previous one. 

```python
set = {a,b,b,b,c}
#S1
	def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        def dfs(nums, level, subset):
            if level == len(nums):
                res.append(subset)
                return
            dfs(nums, level+1, subset+[nums[level]])
            while level < len(nums) - 1 and nums[level+1] == nums[level]:
                level += 1
            dfs(nums, level+1, subset)
        dfs(nums, 0, [])
        return res
#S2
def subsetsWithDup(nums):
    def dfs(nums, index, subset):
        res.append(subset)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            dfs(nums, i+1, subset+[nums[i]])
    res = []
    nums.sort()
    dfs(nums, 0, [])
    return res
```

Analysis: O(2^n) based on the recursion tree.

It is clearer with the recursion tree:

```
set = {a, b1, b2, c}
# S1
					None
		     /					\
a:			a					None
	 	  /		  \				/	  \
b1:       ab1			 a		   b1	     	 None
		/  \   		     |        /   \           |    
b2:   ab1b2	   ab1		 |       b1b2   b2        |
	  /  \     /  \	     / \	/ \	   / \		 /  \	
c:ab1b2c ab1b2 ab1c	ab1 ac  a b1b2c b1b2 b2c b2 c   None

# S2
				    None
			/  		  |			\
pos0		a		  b1		c
		  /	  \		  /  \		
pos1	 ab1   ac    b1b2 b1c
		 /  \		  |
pos2  ab1b2 ab1c     b1b2c
		|
pos3  ab1b2c
```

