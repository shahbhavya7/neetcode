class Solution:
    
    def helper(self, s, index, current, res):
        
        if index == len(s):
            res.append(current.copy())
            return
        
        current.append(s[index])
        self.helper(s, index + 1, current, res)
        current.pop()
        self.helper(s, index + 1, current, res)

    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        
        self.helper(nums, 0, current, res)
        
        return res