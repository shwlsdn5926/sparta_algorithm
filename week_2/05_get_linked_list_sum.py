class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

# 아래 코드에서 중복을 피하려면 어떻게 해야 할까?

def get_linked_list_sum(linked_list_1, linked_list_2):
    cur_1 = linked_list_1.head
    cur_2 = linked_list_2.head
    list_sum = 0
    while cur_1 and cur_2 is not None:
        list_sum = list_sum * 10 + cur_1.data + cur_2.data
        cur_1 = cur_1.next
        cur_2 = cur_2.next
    return list_sum


linked_list_1 = LinkedList(8)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
