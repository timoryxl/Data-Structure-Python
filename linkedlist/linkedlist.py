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

    def swap_node(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next

        if cur1 and cur2:
            if prev1:
                prev1.next = cur2
            else:
                self.head = cur2

            if prev2:
                prev2.next = cur1
            else:
                self.head = cur1

            cur1.next, cur2.next = cur2.next, cur1.next

        else:
            print('error')
            return

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
        self.head = _reverse_recursive(cur=self.head, prev=None)

    # Assume list has been sorted
    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p.data < q.data:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
        self.head = s

        while p and q:
            if p.data < q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next

        if not p:
            s.next = q
        if not q:
            s.next = p

    def remove_duplicates(self):
        cur = self.head
        prev = None
        cmap = {}
        while cur:
            cmap[cur.data] = cmap.get(cur.data, 0) + 1
            if cmap[cur.data] > 1:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next


if __name__ == '__main__':
    # llist = Linkedlist()
    # llist.append('A')
    # llist.print_node()
    # print('---------')
    # llist.prepend('B')
    # llist.print_node()
    # print('length is', llist.len_iterative())
    # print('---------')
    # llist.insert_after_node(llist.head.next, 'E')
    # llist.print_node()
    # print('length is', llist.len_recursive(llist.head))
    # print('---------')
    # llist.swap_node('B', 'A')
    # llist.print_node()
    # print('---------')
    # llist.delete_node('B')
    # llist.print_node()
    # print('---------')
    # llist.delete_at_position(2)
    # llist.print_node()
    # print('---------')
    # llist.append('E')
    # llist.append('R')
    # llist.append('T')
    # llist.reverse_iterative()
    # llist.print_node()
    # print('---------')
    # llist.reverse_recursive()
    # llist.print_node()
    # print('---------')

    # Merge sorted lists
    # llist1 = Linkedlist()
    # llist2 = Linkedlist()
    #
    # llist1.append(1)
    # llist1.append(5)
    # llist1.append(7)
    # llist1.append(9)
    # llist1.append(10)
    #
    # llist2.append(2)
    # llist2.append(3)
    # llist2.append(4)
    # llist2.append(6)
    # llist2.append(8)
    # llist1.print_node()
    # llist2.print_node()
    # llist1.merge_sorted(llist2)
    # llist1.print_node()

    llist1 = Linkedlist()

    llist1.append(1)
    llist1.append(6)
    llist1.append(1)
    llist1.append(4)
    llist1.append(2)
    llist1.append(2)
    llist1.append(4)
    llist1.remove_duplicates()
    llist1.print_node()






