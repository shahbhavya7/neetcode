
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        # Phase 1: Finding the intersection point of the two runners.
        
        while True:
            slow = nums[slow]  # Move slow pointer by 1 step
            fast = nums[nums[fast]]  # Move fast pointer by 2 steps
            if slow == fast:  # A cycle is detected
                break
            
        # Phase 2: Finding the entrance to the cycle.
        fast = nums[0]  # Reset fast pointer to the start of the array or slow pointer to the start of the array

        while slow != fast:
            slow = nums[slow]  # Move slow pointer by 1 step
            fast = nums[fast]  # Move fast pointer by 1 step
            
        return slow  # The duplicate number is found