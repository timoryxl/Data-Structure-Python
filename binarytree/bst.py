class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print('Already exist')

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
        return False

    def _find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data == cur_node.data:
            return True

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(cur_node.data)
            self._inorder_print_tree(cur_node.right)

    def is_bst_satistfied(self):
        if self.root:
            is_bst = self._is_bst_satistfied(self.root)
            if is_bst is not None:
                return False
        return True

    def _is_bst_satistfied(self, cur_node):
        if cur_node.left:
            if cur_node.data > cur_node.left.data:
                return self._is_bst_satistfied(cur_node.left)
            else:
                return False
        if cur_node.right:
            if cur_node.data < cur_node.right.data:
                return self._is_bst_satistfied(cur_node.right)
            else:
                return False


if __name__ == '__main__':
    bst = BST()
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(5)
    bst.insert(10)
    # print(bst.find(6))
    tree = BST()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    print(tree.is_bst_satistfied())
    print(bst.is_bst_satistfied())
