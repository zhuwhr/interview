[47. Permutations II](https://leetcode.com/problems/permutations-ii/)

Key point: how to skip duplications when making decision of current position

In each level, use a set to store the considered elements. We don't consider duplicated element for the same position.

思路一：排序，开一个数组来记录每个元素是否使用过，每次循环时依然循环所有的元素，当这个元素被使用过时跳过。在同一层时，对于重复的元素，只递归一次。去重方法是，如果当前元素与之前相同时，并且之前的元素没有被使用过，这时说明前面的元素已经被递归过了，这时不应该递归当前元素。如果之前的元素被使用过，这时当前元素也应该被递归。（这里比较绕，是这个思路的难点）

思路二：也是排序。但是这时这种思路的优势就体现出来了：由于我们没有往结果里加任何的元素，只是把所有的元素都摆上，然后交换它们间的顺序；所以，当我们发现有重复元素的时候，我们就不需要交换这组元素的顺序了，因为相同元素换一下都是一样的。也就是说，我们只交换不同元素的顺序就可以了。这样就可以用一个集合来存储当前层的`prefix` ，如果循环时元素出现在集合中，说明之前已经处理过这个元素，所以应该跳过。

```python
#S1
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(temp, used):
            if len(temp) == len(nums):
                res.append(list(temp))
                return
            for i in range(len(nums)):
                if i > 0 and not used[i-1] and nums[i] == nums[i-1]: continue #重复元素只递归第一个
                if not used[i]:
                    used[i] = True
                    temp.append(nums[i])
                    backtrack(temp, used)
                    temp.pop()
                    used[i] = False
        
        res = []
        used = [False] * len(nums)
        nums.sort()
        backtrack([], used)
        return res
#S2
def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index):
            if index == len(nums):
                res.append(list(nums))
            prefix_set = set()
            for i in range(index, len(nums)):
                if nums[i] not in prefix_set:
                    prefix_set.add(nums[i])
                    nums[index], nums[i] = nums[i], nums[index]
                    dfs(nums, index+1)
                    nums[index], nums[i] = nums[i], nums[index]
        res = []
        dfs(nums, 0)
        return res
```

Analysis: O(n!)