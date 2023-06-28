'''
225.

Implement a last-in-first-out (LIFO) stack using only two queues. 

The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, 

which means that only push to back, peek/pop from front, size and is empty operations are valid.

Depending on your language, the queue may not be supported natively. 

You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?
'''

## Using two queues
from collections import deque

class MyStack1:

    def __init__(self):

        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:

        self.queue_in.append(x)


    def pop(self) -> int:

        if self.empty():
            return None

        for _ in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in    
        return self.queue_out.popleft()

    def top(self) -> int:

        if self.empty():
            return None
        
        return self.queue_in[-1]


    def empty(self) -> bool:

        return len(self.queue_in) == 0
    
## Using only one queue
    
class MyStack2:

    def __init__(self):

        self.queue = deque()

    def push(self, x):

        self.queue.append(x)

    def pop(self):

        if self.empty():
            return
        for _ in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self):
        
        if self.empty():
            return 
        ans = self.pop()
        self.push(ans)
        return ans
    
    def empty(self):

        return not self.queue