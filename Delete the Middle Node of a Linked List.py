class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None or head == None:
            return None

        slow=head
        fast=head.next
        previous=None

        while fast:
            previous=slow
            slow=slow.next
             
            if fast.next:
                fast=fast.next.next
            else :
                fast=None



        # print(" final previous :",previous)
        previous.next=previous.next.next
        return head    