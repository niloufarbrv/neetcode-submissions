from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

       Input: nums = [1,2,4,6]
       prefix_multiplication=[1]*len(nums)
       postfix_multiplication=[1]*len(nums)
       #iterate over nums for bilding prefix_multiplication
       for i in range(len(nums)):
            if i == 0:
                prefix_multiplication[i]=1
            else:
                prefix_multiplication[i] = nums[i-1] * prefix_multiplication[i-1]

        #iterate over nums for bilding postfix_multiplication
       for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                postfix_multiplication[i] = 1
            else:
                postfix_multiplication[i] = postfix_multiplication[i+1]*nums[i+1]

       final_list = []
       for i in range(len(nums)):
            final_list.append(postfix_multiplication[i]*prefix_multiplication[i])


       return final_list