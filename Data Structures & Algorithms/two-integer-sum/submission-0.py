class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 7
        # first = 3 >>> second7-3 = 4 >>> add 3 to set >> {3:i}
        # first = 4 >>> second = 7-4 = 3
        previous_items = {}
        for index, item in enumerate(nums):
            second_item = target - item
            if second_item in previous_items:
                return [previous_items[second_item], index]
            else:
                previous_items[item] = index
