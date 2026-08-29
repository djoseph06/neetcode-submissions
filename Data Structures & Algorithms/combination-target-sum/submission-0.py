class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        
        result = []
        combination = []

        def backtrack(i, sum):
            if sum == target:
                result.append(combination.copy())
                return
            
            if i == len(nums) or sum > target: 
                return
            
            combination.append(nums[i])
            backtrack(i, sum + nums[i])

            combination.pop()

            backtrack(i + 1, sum)

        backtrack(0,0)
        return result
            

        








        