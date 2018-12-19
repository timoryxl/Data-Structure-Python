class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                cur.next.prev = new_node
                new_node.next = cur.next
                cur.next = new_node
                new_node.prev = cur
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                cur.prev.next = new_node
                new_node.prev = cur.prev
                new_node.next = cur
                cur.prev = new_node
                return
            cur = cur.next


if __name__ == '__main__':
    dllist = DoublyLinkedList()
    dllist.prepend(1)
    dllist.append(2)
    # dllist.prepend(7)
    dllist.append(3)
    dllist.append(4)
    dllist.append(5)
    # dllist.add_after_node(1, 11)
    # dllist.add_after_node(2, 12)
    # dllist.add_after_node(4, 14)
    dllist.add_before_node(2, 11)
    dllist.add_before_node(1, 11)
    dllist.print_list()
