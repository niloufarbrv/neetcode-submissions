class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {1:1, 2:2, 3:3}# counting o(n^2) sorting (nlogn) o(n)

        
        counter = {}
        #o(n)
        for num in nums:
            counter[num] = counter.get(num,0) + 1

        nums_index_by_count = [[] for _ in range(len(nums)+1)]
        #o(n)
        for num, count in counter.items():
            nums_index_by_count[count].append(num)
    
        k_frequent = []
        for i in range(len(nums_index_by_count)-1, 0, -1):
            nums = nums_index_by_count[i]
            for num in nums:
                if k > 0:
                    k_frequent.append(num)
                    k -=1
                else:
                    return k_frequent
        return k_frequent


            








        