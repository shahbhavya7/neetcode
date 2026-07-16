class Solution:
    
    def findCombination(self, index, target, arr, ans, combination):
        if target == 0:
            ans.append(combination.copy())
            return

        if index == len(arr) or target < 0:
            return
        
        combination.append(arr[index])
        self.findCombination(index, target-arr[index], arr, ans, combination)
        combination.pop()
        self.findCombination(index+1, target, arr, ans, combination)
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        
        self.findCombination(0, target, candidates, ans, combination)
        return ans