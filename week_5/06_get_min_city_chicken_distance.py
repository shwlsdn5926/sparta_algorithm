import itertools, sys
from itertools import combinations


n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    location_home = []
    location_chicken = []
    chicken_dist = []
    # 집과 치킨집의 좌표 추출
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                location_home.append([i, j])
            elif city_map[i][j] == 2:
                location_chicken.append([i, j])
    chicken_location_m_combinations = list(itertools.combinations(location_chicken, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in location_home:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            city_chicken_distance += min_home_chicken_distance

        min_distance_of_m_combinations=min(min_distance_of_m_combinations, city_chicken_distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
