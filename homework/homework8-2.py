class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        boo = self.queue[0]
        self.queue = self.queue[1:]
        return boo

    def isEmpty(self):
        return (self.queue ==[])

def main():
    queue = Queue()
    print "Enqueuing..."
    x = raw_input("Enter a string: ")
    while x != "":
        queue.enqueue(x)
        x = raw_input("Enter a string: ")
    print "Dequeuing..."
    while not queue.isEmpty():
        print queue.dequeue()

if __name__ == "__main__":
    main()
