shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not is_existing_target_number(order, menus):
            return False
    return True

def is_existing_target_number(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_average = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if array[cur_average] == target:
            return True
        elif array[cur_average] < target:
            cur_min = cur_average + 1
        else:
            cur_max = cur_average - 1
        cur_average = (cur_min + cur_max) // 2


result = is_available_to_order(shop_menus, shop_orders)
print(result)

# menus[0]이 orders에 있나요?
# 순차 탐색은 시간복잡도가 O(N)이니까 O(logN)로 줄여보자.
# 이진탐색 기본 구조

# 초기 변수


#   주문              메뉴
# if  < len(menus)//2
# menus = menus[0:len(menus)//2-1]
# menus = menus[len(menus)//2+1:]
