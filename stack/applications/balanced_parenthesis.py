from stack.stack import Stack


def is_match(paren1, paren2):
    cmap = {'{': '}',
            '[': ']',
            '(': ')'}
    return True if cmap.get(paren1) == paren2 else False


def is_paren_balanced(paren_string):
    s = Stack()
    index = 0

    while index < len(paren_string):
        paren = paren_string[index]

        if paren in '{[(':
            s.push(paren)
        else:
            if s.is_empty():
                return False
            else:
                last_paren = s.pop()
                if not is_match(last_paren, paren):
                    return False
        index += 1

    return True


if __name__ == '__main__':
    print(is_paren_balanced('{}'))
    print(is_paren_balanced(']]}'))