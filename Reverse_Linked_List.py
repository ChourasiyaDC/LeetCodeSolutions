class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=None
        temp=head
        while temp!=None:
            current=temp
            temp=temp.next
            current.next=l1
            l1=current
        return l1   