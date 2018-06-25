

def cellname_from_pos(c, r):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[c] + str(r + 1)

def pos_from_cellname(cellname):
    assert(cellname)
    c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(cellname[0])
    r = int(cellname[1:]) - 1
    return (c, r)

def has_cycle(rows):
    visited = set()
    has_cycle = False

    for r, row in enumerate(rows):
        for c, col in enumerate(row):
            cn = cellname_from_pos(c, r)
            if not cn in visited:
                visited.add(cn)
                path = [cn]
                has_cycle |= follow_path(rows, path, visited)
    return has_cycle


def follow_path(rows, path, visited):
    hasCycle = False
    cn = path[-1]
    if not cn:
        return hasCycle
    (c, r) = pos_from_cellname(cn)
    next = rows[r][c]
    if next in path:
        print("cycle", path + [next])
        hasCycle = True
    if next not in visited:
        visited.add(next)
        hasCycle |= follow_path(rows, path + [next], visited)
    return hasCycle


m1 = [["B1", "A1", "C1"]]

m2 = [
  ["B2", "",   "",  "A1"],
  ["",   "C3", "",   ""],
  ["A3", "",   "D4", ""],
  ["",   "",   "",   "A1"]
]

m2 = [
  ["B2", "",   "C2",  "A1"],
  ["",   "C3", "C4",   ""],
  ["A3", "",   "D4", ""],
  ["",   "",   "C1",   "A1"]
]

print("has_cycle:", has_cycle(m1), "m1:", m1)
print("has_cycle:", has_cycle(m2), "m2:", m2)


