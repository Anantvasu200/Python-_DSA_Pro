class Node:
    def __init__(self, value):
        self.data = value
        self.next = None  # Corrected "self.Next" to "self.next" for consistency

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):  # Corrected method name "Traverse" to "traverse" for consistency
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.top.data

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            popped_data = self.top.data
            self.top = self.top.next
            return popped_data

def reverse_string(text):
    s = Stack()
    for char in text:
        s.push(char)
    
    result = ""
    while not s.is_empty():
        result += s.pop()
    
    return result

# Example usage:
input_text = "Hello, world!"
reversed_text = reverse_string(input_text)
print("Original Text:", input_text)
print("Reversed Text:", reversed_text)
