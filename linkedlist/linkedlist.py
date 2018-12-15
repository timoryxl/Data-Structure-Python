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

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None

        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            print('Error')
            return

        prev_node.next = cur_node.next
        cur_node = None

    def delete_at_position(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        index = 0
        while cur_node and index < pos:
            prev_node = cur_node
            cur_node = cur_node.next
            index += 1

        if cur_node is None:
            print('Error')
            return

        prev_node.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count+=1
            cur_node = cur_node.next

        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


if __name__ == '__main__':
    llist = Linkedlist()
    llist.append('A')
    llist.print_node()
    print('---------')
    llist.prepend('B')
    llist.print_node()
    print('length is', llist.len_iterative())
    print('---------')
    llist.insert_after_node(llist.head.next, 'E')
    llist.print_node()
    print('length is', llist.len_recursive(llist.head))
    print('---------')
    llist.delete_node('B')
    llist.print_node()
    print('---------')
    llist.delete_at_position(2)
    llist.print_node()


