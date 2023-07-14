# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # curr=head
        # array=[]
        # while curr:
        #     array.append(curr.val)
        #     curr=curr.next
        # loop_val=math.floor(len(array)//k)
        # i,j=0,0
        # while j<loop_val:
        #     array[i:i+k]=reversed(array[i:i+k])
        #     i+=k
        #     j+=1
        # dummy=curr=ListNode(-1)
        # for val in array:
        #     curr.next=ListNode(val)
        #     curr=curr.next
        # return dummy.next


        #### Here is the problem statement ####
        #### You cannot change the values but only nodes of the LinkedList ####

        def reverseLL(p1):
            ## reverse these p1 and p2
            revHead=p1
            pre=ListNode(0)
            post = revHead.next
            while post:
                revHead.next=pre
                pre=revHead
                revHead=post
                post=post.next
            revHead.next=pre
            return revHead

        if k<=1:
            return head
        
        ## Appending 1 ListNode from front
        b=ListNode(-1)
        b.next=head

        # deciding p1 and p2 point value in LL
        pre=b
        p1=p2=head
        post=tail=ListNode(-10)
        
        while p1 and p2.next:

            ## Putting P2 in its place
            loop=k-1
            while loop and p2:
                p2=p2.next
                loop-=1
            if not p2:
                break

            ## Setting up Post P2 pointer
            post=p2.next

            #severed the connection of p1 and p2 from the rest of the LinkedList
            p2.next=None
            pre.next=None

            ## Calling the reversal function
            reverseLL(p1)

            ## Now P2 becomes Head List and p2 becomes Tail of Reversed Linked
            p1.next=post
            pre.next=p2
            pre=p1
            p1=p2=post


        return b.next



