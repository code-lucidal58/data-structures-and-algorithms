"""
Floyd’s Cycle-Finding Algorithm is used to detect loops in linked lists.
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def detect_loop(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add(self, pos):
        last = self.head
        while last.next:
            last = last.next
        pos = pos - 1
        temp = self.head
        while pos:
            temp = temp.next
            pos -= 1
        last.next = temp


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.push(x)
        loop = int(input())
        if (loop):
            a.add(loop)
        print(detect_loop(a.head))  # Linked List Class