class Solution:

    def backtrack(self, nums, idx, res):
        if idx == len(nums):
            res.append(nums.copy())
            return
        
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1, res)
            nums[idx], nums[i] = nums[i], nums[idx]    

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, res)
        return res