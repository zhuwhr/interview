[46. Permutations](https://leetcode.com/problems/permutations/)

思路一：递归树每层代表结果中当前position放置哪种元素。每次循环所有输入元素，当元素不在当前结果中，说明没有被使用过，继续递归。

思路二：递归树意义同上，但是每次递归的时候，不再是选择放入哪个元素，而是假设所有元素都在，每层交换该位置元素与后续元素的位置。这种思路在有重复的时候非常好用。

Idea: When all element must exists in the final solution, we need to put all of them in the solution and only change its sequence.

```
Recursion Tree:
Level -> position (who should be at this position)
Branches -> remaining elements
list = [a,b,c]
						None
				/		  |			\
pos0          abc        bac        cba
			/    \      /   \       /   \
pos1       abc 	 acb   bac  bca    cba  cab
			|     |     |    |      |    |
pos2	   abc   acb   bac  bca    cba  cab 		
```

```python
    def permute(self, nums):
        res = []
        def dfs(nums, index):
            if index == len(nums):
                res.append(list(nums))
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(nums, index+1)
                nums[index], nums[i] = nums[i], nums[index]
        dfs(nums, 0)
        return res

'''iteration  太残暴了
    def permute(self, nums):
        if nums is None:
            return []
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations
    '''
```

Analysis: O(n!)		n x (n-1) x (n-2)  x… x 1

