class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        
        i=0
        d1={}
        max=0
        n=0
        temp=head

        while temp:
            n=n+1
            temp=temp.next

        while head:
            d1[i]=head.val
            head=head.next
            twin=n-1-i
            temp=d1.get(twin,0)   #checking whether value exists in dictionary or not
            value=temp+d1[i]
            i=i+1
            if value >max:
                max=value

        return max
