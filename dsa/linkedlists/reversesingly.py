def reverse(head):

    current = head
    previous = None
    nextnode = None


    while current:

        nextnode = current.nextnode

        current.nextnode = previous

        previous = current

        current = nextnode

    return previous

class Node:

    def __init__(self,value):

        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
print()
reverse(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)








