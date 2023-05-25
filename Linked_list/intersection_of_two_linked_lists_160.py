'''
160.

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 

If the two linked lists have no intersection at all, return null. 

Note that the linked lists must retain their original structure after the function returns.

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
'''

## O(n + m) and O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        size_A = 0
        size_B = 0
        node_A = headA
        node_B = headB
        while node_A:
            size_A += 1
            node_A = node_A.next
        
        while node_B:
            size_B += 1
            node_B = node_B.next

        node_A = headA
        node_B = headB
        if size_A > size_B:
            for _ in range(size_A - size_B):
                node_A = node_A.next
        else:
            for _ in range(size_B - size_A):
                node_B = node_B.next
        
        while node_A:
            if node_A == node_B:
                return node_A
            else:
                node_A = node_A.next
                node_B = node_B.next
        
        return 
        
