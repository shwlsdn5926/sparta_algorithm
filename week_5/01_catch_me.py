from collections import deque

c = 11
b = 4


def catch_me(cony_loc, brown_loc):
    cony_queue = deque()
    cony_queue.append(cony_loc)

    brown_queue = deque()
    brown_queue.append(brown_loc)

    t = 0
    while 0 <= cony_queue[0] <= 200000 and 0 <= brown_queue[0] <= 200000:

        t += 1
        if brown_queue[0] < cony_queue[0] and brown_loc * 2 <= 200000:
            brown_loc *= 2
            cony_loc += t * (t + 1) / 2
            brown_queue.appendleft(brown_loc)
            cony_queue.appendleft(cony_loc)
            if brown_queue[0] == cony_queue[0]:
                return t
            else:
                break
        elif brown_queue[0] == cony_queue[0]:
            return t-1
        elif brown_queue[0] > cony_queue[0] and brown_loc - 1 >= 0:
            brown_loc -= 1
            cony_loc += t * (t + 1) / 2
            brown_queue.appendleft(brown_loc)
            cony_queue.appendleft(cony_loc)
            if brown_queue[0] == cony_queue[0]:
                return t
            else:
                break

print(catch_me(c, b))  # 5가 나와야 합니다!
