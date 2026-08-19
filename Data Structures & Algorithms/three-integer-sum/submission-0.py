class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            num1 = nums[i]
            filtered = nums[:i] + nums[i + 1:]


            top = 0
            bot = len(nums) - 2
            run = True
            while run:
                if bot <= top:
                    run = False

                elif (num1 + filtered[top] + filtered[bot] == 0) and (sorted([num1, filtered[top], filtered[bot]]) not in output):
                    output.append(sorted([num1, filtered[top], filtered[bot]]))
                    bot = bot - 1

                elif num1 + filtered[top] + filtered[bot] > 0:
                    bot = bot - 1

                else:
                    top = top + 1

        return output
                

