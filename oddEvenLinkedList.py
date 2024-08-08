class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp=head
        current=head
        previous=None

        n=0

        while temp!=None:
            previous=temp
            n=n+1         
            temp=temp.next
            
        if n<=2:
            return head
        middle=n//2
        n=1

        while n<=middle:
            second=current.next
            current.next=current.next.next
            second.next=None
            previous.next=second
            previous=previous.next 
            current=current.next
            n=n+1

        return head        
