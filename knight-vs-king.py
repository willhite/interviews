ROW = 0
COL = 1


def chess_board(king, knight, n):
    cntr = 0

    def dfs(knight, n, numMove):
        nonlocal cntr
        indent = '                 '[:2 * numMove]
        print(indent, 'cntr:', cntr, 'knight:', knight, 
            'limit:', n, 'numMove:', numMove)
        cntr += 1
        if numMove > n:
            return 0
        if not is_pos_valid(knight):
            return 0
        if knight == king:
            print(indent, 'FOUND ONE!')
            return 1
        next_positions = get_next_positions(knight)
        print(indent, 'knight', knight, 
            'next_positions:', next_positions)
        result = 0
        for next_knight in next_positions:
            result += dfs(next_knight, n, numMove + 1)
        return result

    # visited = set()
    print('calling dfs')
    return dfs(knight, n, 0)


def get_next_positions(knight):
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
         [1, 2], [1, -2], [-1, 2], [-1, -1]]
    res = []
    for m in moves:
        pos = new_pos(knight, m)
        if is_pos_valid(pos):
            res.append(pos)
    return res


def new_pos(pos, move):
    pos1 = []
    pos1.append(pos[ROW] + move[ROW])
    pos1.append(pos[COL] + move[COL])
    return pos1


def is_pos_valid(pos):
    return pos[ROW] >= 0 and pos[ROW] < 8 and pos[COL] >= 0 and pos[COL] < 8


print('num:', chess_board([3, 7], [0, 4], 2))
