from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_non_zero = 1
        final_result = []

        for item in nums:
            if item == 0:
                zero_count += 1
            else:
                product_non_zero *= item

        for item in nums:
            if zero_count > 1:
                final_result.append(0)
            elif zero_count == 1:
                if item == 0:
                    final_result.append(product_non_zero)
                else:
                    final_result.append(0)
            else:
                final_result.append(product_non_zero // item)

        return final_result