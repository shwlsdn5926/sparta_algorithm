current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


def get_d_index_when_go_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_cleaned = 1  # 청소한 칸의 개수를 counting한다.
    room_map[r][c] = 2  # 청소한 칸에는 2를 저장한다.
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)  # 이게 뭐지???
        cur_d = d

        for i in range(4):
            cur_d = get_d_index_when_rotate_to_left(cur_d)  # 회전 후 방향, 위치를 현재의 그것에 저장한다.
            new_r = r + dr[cur_d]
            new_c = c + dc[cur_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:  # 회전 후 방향, 위치를 현재의 그것에 저장한다.
                count_of_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, cur_d])
                break  # 이미 청소가 되어 있다면 조건문을 빠져나온다.

            elif i == 3:  # 더 이상 갈 곳이 없는 경우 후진한다.
                new_r = r + dr[get_d_index_when_go_back(d)]
                new_c = c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r, new_c, d])
                if room_map[new_r][new_c] == 1:  # 후진했음에도 불구하고 벽에 부딪힌 경우 청소를 끝낸다.
                    return count_of_cleaned


print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
