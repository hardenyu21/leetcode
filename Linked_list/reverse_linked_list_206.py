'''
206.

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].

-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1(object):
    def reverseList_iter(self, head):
        """
        iteratively reverse

        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        result = None
        
        while node is not None:
            result = ListNode(node.val, next = result)
            node = node.next
        
        return result

## Optimization?
class Solution2(object):
    def reverseList_iter(self, head):
        """
        iteratively reverse

        :type head: ListNode
        :rtype: ListNode
        """
        result = None
        node = head

        while node is not None:
            next = node.next
            node.next = result
            result, node = node, next
        
        return result


## Recursive
class Solution3(object):

    def reverseList_recur(self, head):
        return self.reverse(head, None)
    
    def reverse(self, cur, pre):
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)