class Node {
    int value;
    Node text;

    Node(int value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    void insertAtEnd(int value) {
        Node newNode = new Node(value);

        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;
        while (current.next != null) {
            current = current.next;
        }

        current.next = newNode;
    }

    void printRecursive(Node node) {
        if (node == null) return;

        System.out.print(node.value);  // Imprime sem usar +
        printRecursive(node.next);
    }
}