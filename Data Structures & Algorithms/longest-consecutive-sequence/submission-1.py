class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # max_length =1 
        if not nums:
            return 0

        unique_nums = set(nums)
        max_length = 1
        for num in unique_nums:
            if (num-1) in unique_nums:
                continue
            else:
                length = 1
                next_num = num+1
                while next_num in unique_nums:
                    length += 1
                    max_length = max(max_length,length)
                    next_num += 1
        return max_length

