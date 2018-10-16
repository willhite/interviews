class Node(object):
    leftm = {}
    rightm = {}
    topm = {}
    bottomm = {}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def update_less(self, m, row, col):
        if row not in m:
            m[row] = (col, self.value)
        else:
            tup = m[row]
            if tup[0] > col:
                m[row] = (col, self.value)

    def update_greater(self, m, row, col):
        if row not in m:
            m[row] = (col, self.value)
        else:
            tup = m[row]
            if tup[0] < col:
                m[row] = (col, self.value)

    def traverse(self, row, col):
        self.update_less(Node.leftm, row, col)
        self.update_greater(Node.rightm, row, col)
        self.update_less(Node.topm, col, row)
        self.update_greater(Node.bottomm, col, row)
        if self.left:
            self.left.traverse(row + 1, col - 1)
        if self.right:
            self.right.traverse(row + 1, col + 1)


test = Node("a",
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

print("\nleft")
for k, v in Node.leftm.items():
    print("k:", k, "v:", v)

print("\nright")
for k, v in Node.rightm.items():
    print("k:", k, "v:", v)

print("\ntop")
for k, v in Node.topm.items():
    print("k:", k, "v:", v)

print("\nbottom")
for k, v in Node.bottomm.items():
    print("k:", k, "v:", v)

        a
      /   \
    b       c
  /   \       \
d       e       f
              /
            g