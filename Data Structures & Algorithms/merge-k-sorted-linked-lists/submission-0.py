class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
        while len(lists) > 1: # loop until we have only one list left
            temp = []
            for i in range(0, len(lists), 2): 
                # 0 to len(lists) with step of 2 means we take two lists at a time, specifying step helps us to avoid index out of range error
                # if there is odd number of lists, then the last list will be merged with None, which will return the last list itself,
                # so that will be added to temp, and in the next iteration of while loop, it will be merged with the second last list,
                # and so on until we have only one list left
                list1 = lists[i]
                list2  = lists[i + 1] if (i + 1) < len(lists) else None # python allows to check conditions for list in one line
                temp.append(self.mergeTwoLists(list1, list2)) # merge two lists and append the merged list to temp
            lists = temp # this will update the lists with the merged lists, we will repeat this process after every iteration of the while loop until we have only one list left which will be our final merged list
        return lists[0] # return the merged list
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0) 
        cur = dummy 
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next