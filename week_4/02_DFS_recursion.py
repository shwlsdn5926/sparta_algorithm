# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
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
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    # graph에서 key: cur_node에 대응되는 value: adjacent_graph[cur_node]의 모든 adjacent_node에 대하여
    for adjacent_node in adjacent_graph[cur_node]:
        # adjacent_node가 방문한 노드 배열 visited_array에 들어있지 않다면
        if adjacent_node not in visited_array:
            # cur_node를 adjacent_node로 옮겨서 dfs_recursion을 재귀호출한다.
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)


dfs_recursion(graph, 1, visited)
print(visited)
