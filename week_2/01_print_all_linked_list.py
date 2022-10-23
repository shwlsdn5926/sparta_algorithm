class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        # self.head.next = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            # print("cur is", cur.data)
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            # cur의 다음 노드를 cur에 업데이트한다.
            cur = cur.next


Linked_List = LinkedList(3)
Linked_List.append(4)
Linked_List.append(5)

Linked_List.print_all()
