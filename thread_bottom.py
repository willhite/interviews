class Node(object):
    spaces = "                          "
    lnodes = []
    rnodes = []
    tnodes = []
    bnodes = []
    tups = []
    min_y, max_y = 0, 0
    min_x, max_x = 0, 0

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

    def thread_bottom(self, thread):
        added = False
        if not self.left:
            thread.append(self.value)
            added = True
        if self.left:
            self.left.thread_bottom(thread)
        if self.right:
            self.right.thread_bottom(thread)
        if not self.right and not added:
            thread.append(self.value)

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


# a
#   b
#     d
#       None
#       None
#     e
#   c
#     None
#     f
#       g
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
thread = []
test.thread_bottom(thread)
print("thread_bottom:", thread)
