from stack.stack import Stack


def reverse_string(input_string):
    s = Stack()
    for i in input_string:
        s.push(i)

    rev_string = ''
    while not s.is_empty():
        rev_string = rev_string + (s.pop())

    return rev_string


if __name__ == '__main__':
    string = 'adfsdf'
    print(reverse_string(string))