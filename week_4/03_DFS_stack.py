graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    # '방문한 노드 배열에 저장 -> 현재 노드와 인접한 노드를 스택에 저장' 패턴 반복하기
    while stack:
        # '스택의 마지막 원소 -> 방문 노드로 저장'이 반복의 시작!
        cur_node = stack.pop()
        visited.append(cur_node)
        # 현재 노드와 인접한 노드를 모두 스택에 저장하기!
        for adjacent_node in adjacent_graph[cur_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited

print(dfs_stack(graph, 1))