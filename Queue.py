class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    # Smart coding "self.front == None" to "self.front is None" for consistency
    
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
    # Smart coding "self.front == None" to "self.front is None" for consistency
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def traverse(self):
        temp = self.front
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.front.value
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            popped_data = self.front.value
            self.front = self.front.next
            return popped_data

My_object = Queue()

My_object.enqueue(100)
My_object.enqueue(200)
My_object.enqueue(300)
My_object.enqueue(400)
My_object.enqueue(500)


print("My queue after enqueue:", My_object.traverse())


print("Dequeued element:", My_object.dequeue())

print("My queue after dequeue:", My_object.traverse())

