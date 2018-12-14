class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print_node(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)

        if not prev_node:
            print('error')
            return

        new_node.next = prev_node.next
        prev_node.next = new_node


if __name__ == '__main__':
    llist = Linkedlist()
    llist.append('A')
    llist.print_node()
    print('---------')
    llist.prepend('B')
    llist.print_node()
    print('---------')
    llist.insert_after_node(llist.head.next, 'E')
    llist.print_node()


