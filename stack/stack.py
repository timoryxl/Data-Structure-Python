class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return []
        else:
            return self.items[-1]

    def get_stack(self):
        return self.items

    def print(self):
        return self.items


if __name__ == '__main__':
    s = Stack()
    s.push('A')
    s.push('B')
    print(s.print())