queue = []

#Add an element to the queue
def enqueue(x):
    queue.append(x)

#Delete an element from the queue
def dequeue():
    if queue:
        return queue.pop(0)
    print("Empty queue")
    return None

enqueue("Ahmed 0546560")
enqueue("Salim 2131260")
print(queue)
x = dequeue()
print(queue)