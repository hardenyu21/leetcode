'''
19.

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##find the length of the list?
##Time: O(N), space: O(1)
class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        head = ListNode(next = head)
        node = head
        while node.next:
            size += 1
            node = node.next

        if n <= 0 or n > size:
            return
        else:
            index = size - n
            node = head.next
            prev = head
            while index:
                prev = node
                node = node.next
                index -= 1
            prev.next = node.next
            return head.next

## Improve?
## One pass
## Time: O(N), Space: O(1)
class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head = ListNode(next = head)
        cur_node = head
        while cur_node.next:
            node = cur_node.next
            for _ in range(n):
                node = node.next
                if node is None:
                    cur_node.next = cur_node.next.next
                    return head.next
            cur_node = cur_node.next


##slow and fast
##One pass: 
##Time: O(N) Space: O(1)
class Solution3(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head = ListNode(next = head)
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head.next