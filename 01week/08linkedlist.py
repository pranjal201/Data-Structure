""" this is a singly linked list program 
TODO: create a singly linked list
and traverse it properly"""


class Node:

    def __init__(self, dataval = None, nextnode = None):
        self.dataval = dataval
        self.nextnode = nextnode


class Slinkedlist:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            print(id(printval))
            printval = printval.nextnode


list1 = Slinkedlist()
list1.headval = Node(4)
e2 = Node(1)
e3 = Node(5)

list1.headval.nextnode = e2
e2.nextnode = e3
temp = list1.headval
list1.print_list()
list1.headval = e2
list1.print_list()

print(temp.dataval)
print(id(temp))
