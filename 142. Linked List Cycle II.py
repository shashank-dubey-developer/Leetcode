# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #### HashMap Method/ Can use set as well ####
        # dictionary={}
        # curr=head
        # while curr:
        #     if curr in dictionary:
        #         return dictionary[curr]
        #     else:
        #         dictionary[curr]=curr
        #     curr=curr.next

        #### Hare and Turtoise method ####
        turtoise=hare=head
        while hare and hare.next:
            turtoise=turtoise.next
            hare=hare.next.next
            if hare == turtoise:
                break
        if not hare or not hare.next:
            return None
        
        hare=head
        while hare!=turtoise:
            hare=hare.next
            turtoise=turtoise.next
        
        return hare
        
