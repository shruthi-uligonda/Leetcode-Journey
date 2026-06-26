# LeetCode 0160 - Intersection of Two Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA and headB:
            return None
        PointerA = headA
        PointerB = headB
        while PointerA != PointerB:
            PointerA = PointerA.next if PointerA else headB
            PointerB = PointerB.next if PointerB else headA
        return PointerA
