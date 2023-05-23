'''
24.

Given a linked list, swap every two adjacent nodes and return its head. 

You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

## O(n)
## O(1)
class ListNode(object):
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next = head)
        node = dummy
        while node.next and node.next.next:
            tmp1 = node.next
            tmp2 = tmp1.next
            tmp3 = tmp2.next
            node.next = tmp2
            tmp2.next = tmp1
            tmp1.next = tmp3
            node = tmp1

        return dummy.next