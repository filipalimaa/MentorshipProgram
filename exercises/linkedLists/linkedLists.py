#Create Node class to represent each node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Create function to feed the linked list
def insert(head, value):
    new_node = Node(value)
    
    if not head:
        return new_node
    
    current = head
    
    while current.next:
        current = current.next
        
    current.next = new_node
    return head

#Recursive function to generate a string
def recursive_string(node):
    if node is None:
        return ""
    return node.value + recursive_string(node.next)