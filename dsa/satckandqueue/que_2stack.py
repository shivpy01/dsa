class Que2Stacks:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enque(self,item):
        self.instack.append(item)


    def deque(self):

        if not self.outstack:
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


q = Que2Stacks()

for i in reversed(range(1,6)):
    q.enque(i)

for i in range(5):
    print(q.deque())
