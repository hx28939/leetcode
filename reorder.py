# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = slow.next
        cur = slow.next.next
        head2 = slow.next
        slow.next = None
        while cur:
            pre.next = cur.next
            cur.next = head2
            head2 = cur
            cur = pre.next
        
        new = ListNode(0)
        new.next = head2
        head2 = new
        
        pre1 = head
        cur1 = head.next
        pre2 = head2
        cur2 = head2.next
        while cur2:
            pre2.next = cur2.next
            pre1.next = cur2
            cur2.next = cur1
            cur2 = pre2.next
            pre1 = cur1
            if pre1 == None:
                break
            cur1 = pre1.next
            
        
                
            
        