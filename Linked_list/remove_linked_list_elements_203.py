'''
203. 

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 

and return the new head.

Example 1:

    Input: head = [1,2,6,3,4,5,6], val = 6

    Output: [1,2,3,4,5]

Example 2:

    Input: head = [], val = 1
    
    Output: []

Example 3:

    Input: head = [7,7,7,7], val = 7

    Output: []
    
Constraints:

    The number of nodes in the list is in the range [0, 104].
    
    1 <= Node.val <= 50
    
    0 <= val <= 50

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

## if node.next_node.val == val --> node.next_node = next_node.next_node --> node = next_node.next_node
## O(n) and O(1)

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        result = ListNode(0, next = head)
        current_node = result

        while current_node.next is not None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return result.next