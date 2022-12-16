#https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stackOne = []

    def push(self, x: int) -> None:
        self.stackOne.append(x)

        

    def pop(self) -> int:
        return self.stackOne.pop(0)
        

    def peek(self) -> int:
        return self.stackOne[0]
        

    def empty(self) -> bool:
        if not self.stackOne:
            return 1
        else:
            return 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()