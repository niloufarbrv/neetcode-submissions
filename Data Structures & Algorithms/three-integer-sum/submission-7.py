class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        #  nums = [-1,0,1,2,-1,-4]
        #[-4, -1, -1, 0, 1, 2] n= 6
        result = []

        for i , a in enumerate(sorted_nums):

            if  i > 0 and a == sorted_nums[i-1]:
                continue

            target = - sorted_nums[i]
            left_poniter, right_poniter = i+1, len(sorted_nums)-1

            while left_poniter < right_poniter:
                if (sorted_nums[left_poniter]+sorted_nums[right_poniter])  == target:
                    result.append([sorted_nums[i], sorted_nums[left_poniter], sorted_nums[right_poniter]])
                    left_poniter += 1
                    right_poniter -= 1
                    while sorted_nums[left_poniter] == sorted_nums[left_poniter-1] and left_poniter < right_poniter:
                        left_poniter += 1

                elif sorted_nums[left_poniter]+sorted_nums[right_poniter] < target:
                    left_poniter += 1
                else:
                    right_poniter -= 1
        return result 


