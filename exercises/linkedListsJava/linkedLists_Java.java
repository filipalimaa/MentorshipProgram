import java.util.Scanner;

class Node {
    int value;
    Node next;

    Node(int value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    void insertAtBeginning(int value) {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
    }

    void printRecursive(Node node) {
        if (node == null) return;

        System.out.print(node.value);  // Imprime sem usar +
        printRecursive(node.next);
    }

    void print() {
        printRecursive(head);
        System.out.println(); // Nova linha no fim
    }
}

public class Main {
    public static void main(String[] args) {
        LinkedList binaryList = new LinkedList();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Insert a number: ");
        int decimal = scanner.nextInt();

        if (decimal == 0) {
            binaryList.insertAtBeginning(0);
        } else {
            while (decimal > 0) {
                int remainder = decimal % 2;
                binaryList.insertAtBeginning(remainder);
                decimal /= 2;
            }
        }
        System.out.print("Binary Number: ");
        binaryList.print();
        scanner.close();
    }
}