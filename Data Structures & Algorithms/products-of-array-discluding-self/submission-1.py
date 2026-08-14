class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = False
        hasZeroes = False
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            elif hasZero == True:
                hasZeroes = True
            else:
                hasZero = True

        out = []
        for i in range(len(nums)):
            if nums[i] == 0 and hasZeroes == True:
                out.append(0)
            elif nums[i] == 0 and hasZero == True:
                out.append(int(product))
            elif nums[i] != 0 and hasZero == True:
                out.append(0)
            else: 
                out.append(int(product/nums[i]))
        
        return out