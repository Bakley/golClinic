def newStack():
    """ Function to create an empty stack"""
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    if size(stack) == 0:
        return True

def push(stack, item):
    """Add an item to stack"""
    stack.append(item)

def pop(stack):
    """Remove an item from stack"""
    if isEmpty(stack): return
    return stack.pop()

def reverse(string):
    n = len(string)

    stack = newStack()

    for i in range(0, n, 1):
        push(stack, string[i])

    string = ""

    for i in range(0, n, 1):
        string += pop(stack)

    return string

string="GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)