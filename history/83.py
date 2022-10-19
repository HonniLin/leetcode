class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        res, res.next = ListNode(0), head
        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res.next