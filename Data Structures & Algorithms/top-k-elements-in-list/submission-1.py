class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                table[nums[i]] += 1
            else:
                table[nums[i]] = 1

        arr = []
        for num, count in table.items():
            arr.append([count, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])                                               

        return res
        
            
