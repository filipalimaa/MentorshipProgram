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

def helper(n, head=None):
    
    if n == 0:
        return head
    head = helper(n // 2, head) 
    head = insert(head, str(n % 2))
    return head

#Function to convert integer to binary
def integer_to_binary(n):

    if n == 0:
        return Node("0")
    return helper(n)

head = integer_to_binary(6)
print(recursive_string(head))