class Node(object):
    spaces = "                          "
    lnodes = []
    rnodes = []
    tnodes = []
    bnodes = []
    tups = []
    min_y, max_y = 0, 0
    min_x, max_x = 100, 0

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def traverse(self, x, y):
        Node.min_x = min(Node.min_x, x)
        Node.max_x = max(Node.max_x, x)
        Node.max_y = max(Node.max_y, y)

        self.tups.append((x, y, self.value))
        y += 1
        if self.left:
            self.left.traverse(x - 1, y)
        if self.right:
            self.right.traverse(x + 1, y)


def left_tups(tups):
    rows = {}
    for t in tups:
        (x, y, v) = t
        if y not in rows:
            rows[y] = v
    return rows
    

def right_tups(tups):
    rows = {}
    for t in tups:
        (x, y, v) = t
        rows[y] = v
    return rows


def top_tups(tups):
    rows = {}
    for t in tups:
        (x, y, v) = t
        if x not in rows:
            rows[x] = v
    return rows


def bottom_tups(tups):
    rows = {}
    for t in tups:
        (x, y, v) = t
        rows[x] = v
    return rows


test = Node(
    "a",
    Node(
        "b",
        Node("d"),
        Node("e")
    ),
    Node(
        "c",
        None, 
        Node(
            "f",
            Node("g"),
            None
        )
    )
)
test.traverse(0, 0)

for x, l in enumerate(test.tups, 0):
    print(x, ":", l)

print("ltups:", left_tups(test.tups))
print("rtups:", right_tups(test.tups))
print("ttups:", top_tups(test.tups))
print("btups:", bottom_tups(test.tups))
