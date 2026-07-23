class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        count = self.countNodes(head)
        if n > count:
            return head
        node_to_remove = count - n + 1 
        if node_to_remove == 1: # if we need to remove the head node then we just return the next node as the new head
            return head.next
        current = head
        current_position = 1
        while current_position < node_to_remove - 1: # we need to stop at the node before the node to remove
            current = current.next
            current_position += 1
        current.next = current.next.next
        return head
   
    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count 