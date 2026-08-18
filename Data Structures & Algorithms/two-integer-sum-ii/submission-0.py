class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        run = True
        while run:
            sum = numbers[front] + numbers[back]
            if sum > target:
                back = back - 1

            elif sum < target:
                front = front + 1

            else:
                return [front + 1, back + 1]