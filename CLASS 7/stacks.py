stack = []

def push(x):
    stack.append(x)

def pop_stack():
    if stack:
        return stack.pop()
    print("Stack is empty.")
    return None

push("A");push("B");push("C")

while stack:
    print(pop_stack())