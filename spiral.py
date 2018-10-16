

def spiral(n):
    if n <= 0:
        return
    print("\nCoordinates for n:", n)
    total = n * n
    mid = n // 2
    print("n:", n, "total:", total, "mid:", mid)
    dir = ["u", "l", "d", "r"]
    dir_idx = 3
    limit = 0
    lim_idx = 0
    x, y = mid, mid
    for i in range(0, total):
        print("(%s, %s), dir: %s, dir_idx: %s, limit:%s, lim_idx: %s" %
            (x, y, dir[dir_idx], dir_idx, limit, lim_idx))
        if lim_idx >= limit:
            # change direction
            dir_idx = (dir_idx + 1) % 4
            if dir[dir_idx] in ["u", "d"]:
                limit += 1
            lim_idx = 0

        lim_idx += 1
        if dir[dir_idx] == "u":
            y -= 1
        elif dir[dir_idx] == "l":
            x -= 1
        elif dir[dir_idx] == "d":
            y += 1
        else:
            x += 1


for n in range(1, 6):
    spiral(n)
