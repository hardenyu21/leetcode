'''
707.

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: val and next. val is the value of the current node, 

and next is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 

Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.

int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.

void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, 

the new node will be the first node of the linked list.

void addAtTail(int val) Append a node of value val as the last element of the linked list.

void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 

If index equals the length of the linked list, the node will be appended to the end of the linked list. 

If index is greater than the length, the node will not be inserted.

void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 
Example:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

'''

##Date: 5.20, still some bugs

##Singlelist node

class SingleListNode():
    def __init__(self, val = None, next = None):
        self.val = val 
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = SingleListNode()   
        self.dummy = SingleListNode(next = self.head)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current_index = 0
        current_node = self.dummy.next
        while current_node is not None:
            if current_index == index:
                return current_node.val
            else:
                current_index += 1
                current_node = current_node.next
        return -1
    
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        next = self.head if self.head.val is not None else None 
        self.head = SingleListNode(val = val, next = next)
        self.dummy = SingleListNode(next = self.head)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current_node = self.dummy.next
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = SingleListNode(val = val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current_index = 0
        current_node = self.dummy.next
        while current_node.next is not None:
            if current_index == index - 1:
                current_node.next = SingleListNode(val = val, next = current_node.next)
                return
            else:
                current_index += 1
                current_node = current_node.next
        if current_index == index - 1:
            current_node.next = SingleListNode(val = val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        current_index = 0
        current_node = self.dummy.next
        if index == 0:
            self.head = SingleListNode(val = self.head.next.val, next = self.head.next)
            self.dummy = SingleListNode(next = self.head)
        else:
            while current_node.next is not None:
                if current_index == index - 1:
                    current_node.next = current_node.next.next
                    break
                else:
                    current_index += 1
                    current_node = current_node.next

## Double linked list

class MyLinkedList(object):

    def __init__(self):
        pass

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """