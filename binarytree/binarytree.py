from stack.stack import Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            val = self.items[0]
            del self.items[0]
            return val

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0].value

    def __len__(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(tree.root, '')
        elif traversal_type == 'reverse_levelorder':
            return self.reverse_levelorder_print(tree.root, '')
        else:
            print('Not Supported')
            return

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def levelorder_print(self, start, traversal):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start, traversal):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while not stack.is_empty():
            node = stack.pop()
            traversal += str(node.value) + '-'
        return traversal

    def height(self, node):
        if node is None:
            return -1
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        return 1 + max(height_left, height_right)

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)

    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while not stack.is_empty():
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)
    # print(tree.print_tree('preorder'))
    # print(tree.print_tree('levelorder'))
    # print(tree.print_tree('reverse_levelorder'))
    # print(tree.height(tree.root))
    # print(tree.size())
    print(tree.size_recursive(tree.root))

