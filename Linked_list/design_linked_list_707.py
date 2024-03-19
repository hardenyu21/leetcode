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

##Date: 5.20, still some bugs, some cases can not pass

##Singlelist node

class SingleListNode():
    def __init__(self, val = None, next = None):
        self.val = val 
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = SingleListNode()   
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        current_node = self.head.next
        while index:
            current_node = current_node.next
            index -= 1
        return current_node.val
    
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = SingleListNode(val = val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = SingleListNode(val = val)
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            self.addAtHead(val = val)
        elif index == self.size:
            self.addAtTail(val = val)
        elif index > self.size:
            pass
        else:
            current_node = self.head
            while index:
                current_node = current_node.next
                index -= 1
            node = SingleListNode(val = val, next = current_node.next)
            current_node.next = node
            self.size += 1
        return

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size or index < 0:
            pass
        else:
            current_node = self.head
            while index:
                current_node = current_node.next
                index -= 1
            current_node.next = current_node.next.next
            self.size -= 1
    

##Double linked list

class DoubleListNode:
    
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        

class MyLinkedList(object):

    def __init__(self):
        self.head = DoubleListNode()
        self.tail = DoubleListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get_node(self, index):
        if index < self.size // 2:
            current_node = self.head.next
            while index:
                current_node = current_node.next
                index -= 1
        else:
            current_node = self.tail.prev
            index = self.size - index - 1
            while index:
                current_node = current_node.prev
                index -= 1
        return current_node

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        else:
            node = self.get_node(index)
            return node.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = DoubleListNode(val = val, next = self.head.next, prev = self.head)
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = DoubleListNode(val = val, prev = self.tail.prev, next = self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            pass
        else:
            node = self.get_node(index)
            added_node = DoubleListNode(val = val, prev = node.prev, next = node)
            node.prev.next = added_node
            node.prev = added_node
            self.size += 1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            pass
        else:
            node = self.get_node(index)
            prev = node.prev  
            next = node.next  
            prev.next, next.prev = next, prev
            self.size -= 1