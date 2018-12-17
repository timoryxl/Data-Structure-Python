class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove_node(self, key):
        if self.head is None:
            print('error')
            return
        elif self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


if __name__ == '__main__':
    cllist = CircularLinkedList()
    cllist.append('C')
    cllist.append('B')
    cllist.prepend('B')
    cllist.prepend('A')
    cllist.remove_node('D')
    cllist.remove_node('B')
    cllist.print_list()
