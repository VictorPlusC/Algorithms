"""
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
# Time complexity: O(1)
# Space complexity: O(N)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            last_min = self.stack[-1][0]
            curr_min = min(x, last_min)
            self.stack.append([curr_min, x])
        else:
            self.stack.append([x, x])

    def pop(self) -> None:
        return self.stack.pop()[1]

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
