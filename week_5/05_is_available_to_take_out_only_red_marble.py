from collections import deque

game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def is_available_to_take_out_only_red_marble(game_map):
    n = len(game_map)
    m = len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1

    # "R", "B"의 현재 위치와 방문 횟수를 queue에 저장한다.
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    # 방문한 위치는 True로 바꾼다.
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == "0":
                continue
            if game_map[next_red_row][next_red_col] == "0":
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
    return False


def move_until_wall_or_hole(r, c, delta_r, delta_c, game_map):
    move_count = 0
    # 다음 위치가 벽 또는 현재 위치가 구멍이 아닐 때 구슬의 위치를 이동시킨다.
    while game_map[r + delta_r][c + delta_c] != "#" and game_map[r][c] != "0":
        r += delta_r
        c += delta_c
        move_count += 1
    return r, c, move_count


print(is_available_to_take_out_only_red_marble(game_map))
