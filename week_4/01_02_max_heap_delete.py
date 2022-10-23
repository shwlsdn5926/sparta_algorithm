class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # def delete(self):
    #     self.items[1], self.items[- 1] = self.items[- 1], self.items[1]
    #     root_node = self.items.pop()
    #     cur_index = 1
    #     while cur_index * 2 < len(self.items) - 1:
    #         left_child_index = cur_index * 2
    #         right_child_index = cur_index * 2 + 1
    #         if self.items[left_child_index] < self.items[right_child_index]:
    #             self.items[right_child_index], self.items[cur_index] = self.items[cur_index], self.items[
    #                 right_child_index]
    #             cur_index = right_child_index
    #         if self.items[left_child_index] > self.items[right_child_index]:
    #             self.items[left_child_index], self.items[cur_index] = self.items[cur_index], self.items[
    #                 left_child_index]
    #             cur_index = left_child_index
    #         if self.items[left_child_index] == self.items[right_child_index]:
    #             break
    #     return root_node

    def delete(self):
        self.items[1], self.items[- 1] = self.items[- 1], self.items[1]
        root_node = self.items.pop()
        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1

            # cur_node, left_child_node, right_child_node 중, max_node의 위치를 max_index라고 놓는다.
            max_index = cur_index

            # cur_index, left_child_index, right_child_index에 위치한 세 노드를 비교한다.
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            # 첫 번째 조건문만 만족했다면, left_child_node가 최대가 된다.
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            # 두 번째 조건문을 만족했다면, right_child_node가 최대가 된다.
            # 위의 if문을 만족시키지 않으므로 노드를 교체할 필요가 없음.
            if max_index == cur_index:
                break

            # 위의 break문을 거치지 않았다면 cur_node <-> max_node 실행
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]

            # 교체된 자식 노드의 위치인 max_index를 cur_index로 변경
            cur_index = max_index

        return root_node


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
max_heap.insert(3)
print(max_heap.items)
print(max_heap.delete())
print(max_heap.items)
