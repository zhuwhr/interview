[31. Next Permutation](https://leetcode.com/problems/next-permutation/)

这个题是考察纯数组的操作，跟permutation一类的题目没有关系。

在当前序列中，从尾端往前寻找两个相邻元素，前一个记为first，后一个记为second，并且满足first 小于 second。然后再从尾端寻找另一个元素number，如果满足first 小于number，即将第first个元素与number元素对调，并将second元素之后（包括second）的所有元素颠倒排序，即求出下一个序列

example:
6，3，4，9，8，7，1
此时 first ＝ 4，second = 9
从尾巴到前找到第一个大于first的数字，就是7
交换4和7，即上面的swap函数，此时序列变成6，3，7，9，8，4，1
再将second＝9以及以后的序列重新排序，让其从小到大排序，使得整体最小，即reverse一下（因为此时肯定是递减序列）
得到最终的结果：6，3，7，1，4，8，9

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        if not nums: return
        # i: lower position to be swaped
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] > nums[i]:
                # j: hight position to be swaped
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
                reverse(nums, i+1, len(nums)-1)
                return
        reverse(nums, 0, len(nums)-1)
```

Analysis O(n) 注意不要弄混成O(n^2)，看似两层循环，但实质上只是把数组扫了两遍，遇到满足条件的就返回了。`reverse`的部分也是O(n)的操作