
def check_brackets(to_check):
    """Verifies matching brackets.

    >>> check_brackets("()")
    True
    >>> check_brackets(")(")
    False
    >>> check_brackets("()[]{}")
    True
    >>> check_brackets("(]")
    False
    >>> check_brackets("")
    True
    >>> check_brackets("([)]")
    False
    """

    if to_check == '':
        return True

    stack = []

    for char in to_check:
        if char in {'[', '(', '{'}:
            stack.append(char)
        else:
            if stack == []:
                return False
            else:
                if stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '(' and char == ')':
                    stack.pop()
                else:
                    return False

    return not stack
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
