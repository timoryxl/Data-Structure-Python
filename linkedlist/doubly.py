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

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    cur.next.prev = None
                    self.head = cur.next
                    cur = None
                    return
            elif cur.data == key:
                if cur.next:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return
                else:
                    cur.prev.next = None
                    cur = None
                    return
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    cur.next.prev = None
                    self.head = cur.next
                    cur = None
                    return
            elif cur == node:
                if cur.next:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return
                else:
                    cur.prev.next = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        cmap = set()
        cur = self.head
        while cur:
            if cur.data in cmap:
                temp = cur.next
                self.delete_node(cur)
                cur = temp
            else:
                cmap.add(cur.data)
                cur = cur.next

    def pairs_with_sum(self, sum_val):
        pairs = []
        p = self.head
        q = None
        while p.next:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append((p.data, q.data))
                    break
                q = q.next
            p = p.next
        return pairs


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
    # dllist.add_before_node(2, 11)
    # dllist.add_before_node(1, 11)
    # dllist.delete(5)
    # dllist.reverse()
    # dllist.append(12)
    # dllist.append(8)
    # dllist.append(6)
    # dllist.append(6)
    # dllist.append(8)
    # dllist.append(12)
    # dllist.append(6)
    # dllist.append(8)
    # dllist.append(12)
    # dllist.append(6)
    # dllist.append(11)
    # dllist.remove_duplicates()
    print(dllist.pairs_with_sum(5))
    #dllist.print_list()
