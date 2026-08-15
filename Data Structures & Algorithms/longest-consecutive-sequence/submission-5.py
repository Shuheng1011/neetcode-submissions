class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        if len(number) == 1:
            return 1

        if len(number) == 0:
            return 0

        glen = 1
        for n in number:
            if (n - 1) not in number:
                i = 1
                lens = 0
                while (n + i) in number:
                    lens = i + 1 
                    i = i + 1
                    if (lens > glen):
                        glen = lens
        return glen