class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        # 마지막 요소에 새로운 값을 추가한다.
        self.tail.next = new_node
        # 새로운 요소를 마지막 요소로 정한다.
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"

        head_node = self.head
        self.head = self.head.next
        return head_node.data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())