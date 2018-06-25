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

    def __str__(self):
        return (
            "lnodes: " + str(self.lnodes) + "\n" +
            "rnodes: " + str(self.rnodes) + "\n" +
            "tnodes: " + str(self.tnodes) + "\n" +
            "bnodes: " + str(self.bnodes) + "\n" +
            "x: (%s, %s)" % (self. min_x, self.max_x) + " "
            "y: (%s, %s)" % (self. min_y, self.max_y)
        )

    def views(self, x, y):
        Node.min_x = min(Node.min_x, x)
        Node.max_x = max(Node.max_x, x)
        Node.max_y = max(Node.max_y, y)

        self.tups.append((x, y, self.value))
        y += 1
        if self.left:
            self.left.views(x-1, y)
        if self.right:
            self.right.views(x+1, y)
    
    def print(self, level):
        print("{}{}".format(self.spaces[0:level*2], self.value))
        if self.left:
            self.left.print(level+1)
        else:
            print("{}None".format(self.spaces[0:(level+1)*2]))
        if self.right:
            self.right.print(level+1)
        else:
            print("{}None".format(self.spaces[0:(level+1)*2]))


def left_tups(tups, min_x, max_x, min_y, max_y):
    mins = [max_x + 10] * (max_y + 1)
    res = [None] * (max_y + 1)
    for t in tups:
        (x, y, v) = t
        if x < mins[y]:
            mins[y] = x
            res[y] = v
            print("mins:", mins)
            print("res:", res)
    return res
        
def right_tups(tups, min_x, max_x, min_y, max_y):
    maxs = [-1] * (max_y + 1)
    res = [None] * (max_y + 1)
    for t in tups:
        (x, y, v) = t
        if x > maxs[y]:
            maxs[y] = x
            res[y] = v
    return res
        
def top_tups(tups, min_x, max_x, min_y, max_y):
    num = (max_x - min_x)
    mins = [max_y + 10] * (num + 1)
    offset = 0-min_x
    res = [None] * (num + 1)
    for t in tups:
        (x, y, v) = t
        if y < mins[x+offset]:
            mins[x+offset] = y
            res[x+offset] = v
    return res

def bottom_tups(tups, min_x, max_x, min_y, max_y):
    num = (max_x - min_x)
    maxs = [-1] * (num + 1)
    offset = 0-min_x
    res = [None] * (num + 1)
    for t in tups:
        (x, y, v) = t
        if y > maxs[x+offset]:
            maxs[x+offset] = y
            res[x+offset] = v
    return res


# 1
#   2
#     4
#       None
#       None
#     5
#   3
#     None
#     6
#       7
#         None
#         None
#       None

test = Node("a", 
    Node("b", 
        Node("d"),
        Node("e")
    ),
    Node("c", 
        None, 
        Node("f",
            Node("g"),
            None
        )
    )
)
test.print(0)
test.views(0, 0)

for x, l in enumerate(test.tups, 0):
    print(x, ":", l)

print("ltups:", left_tups(test.tups, test.min_x, test.max_x, test.min_y, test.max_y))
print("rtups:", right_tups(test.tups, test.min_x, test.max_x, test.min_y, test.max_y))
print("ttups:", top_tups(test.tups, test.min_x, test.max_x, test.min_y, test.max_y))
print("btups:", bottom_tups(test.tups, test.min_x, test.max_x, test.min_y, test.max_y))
