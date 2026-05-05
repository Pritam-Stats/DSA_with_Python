#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head
        
        #make it circular
        tail.next = head

        curr = head
        for _ in range(n-k-1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        return new_head

        


# @lc code=end

