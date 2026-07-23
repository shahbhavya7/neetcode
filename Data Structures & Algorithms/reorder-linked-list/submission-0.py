class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second_half = self.reverseList(slow.next) # seconf half has head of the reversed second half of the list
        slow.next = None # now as list is reversed slow's next will be the last node of the list so we need to set it to None
        first_half = head # first half has head of the first half of the list

        while second_half:
            temp1,temp2 = first_half.next, second_half.next # we need to store the next nodes of first half and second half before changing the next pointers
            first_half.next = second_half # we need to point the next of first half to the current node of second half
            second_half.next = temp1 # we need to point the next of current node of second half to the next node of first half
            first_half = temp1 # we need to move the first half pointer to the next node of first half
            second_half = temp2 # we need to move the second half pointer to the next node of second half
   
    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count 
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current  = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current  = next_node
        return prev