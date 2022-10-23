top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    n = len(heights)
    orders = [0] * n

    while heights:
        height = heights.pop()

        for i in range(len(heights) - 1, 0, -1):
            if height < heights[i]:
                orders[len(heights)] = i + 1
                break

    return orders


print(get_receiver_top_orders(top_heights))
