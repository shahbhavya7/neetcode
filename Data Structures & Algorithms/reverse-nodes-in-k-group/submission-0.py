class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while count < k: # check if there are at least k nodes left in the linked list, if not, return the head as is, no need to reverse the remaining nodes 
            if not temp:
                return head
            temp = temp.next
            count += 1
            
        new_head = self.reverseKGroup(temp, k) # reverse the next k nodes recursively and get the new head of the reversed list
        
        temp = head
        count = 0
        while count < k: # reverse the current k nodes
            next_node = temp.next
            temp.next = new_head
            new_head = temp
            temp = next_node
            count += 1
            
        return new_head # return the new head of the reversed list