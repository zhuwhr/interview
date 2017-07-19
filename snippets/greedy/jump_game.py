'''
https://leetcode.com/problems/jump-game/#/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Idea: 
Greedy
'''


def canJump(nums):
    reach = 0
    for i in range(len(nums)):
        if i > reach: return False
        reach = max(reach, i + nums[i])
    return True


# follow up: min steps need to jump
'''
Jump from the first index, 
do not make a jump choice until trying every possibility of the reachable points from the current one. 
After trying every poosibility, update the jump ability 
by maintaining a max_reach variable (max_reach - curr index)
'''
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    jump = 0
    ability = 1  # the ability to jump at current point
    reach = 0
    # do not care about the last one, we only need to know the second last one's ability is not 0,
    # or we have to make one more jump
    for i in range(0, len(nums) - 1):
        reach = max(reach, nums[i] + i)
        ability -= 1
        if ability == 0:  # checked all possibility, need to make a jump decision
            ability = reach - i
            jump += 1  # jump at the point which gives the max reach point.
    return jump