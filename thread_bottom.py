import string

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
        self.next = None

    def __str__(self):
        return (
            "lnodes: " + str(self.lnodes) + "\n" +
            "rnodes: " + str(self.rnodes) + "\n" +
            "tnodes: " + str(self.tnodes) + "\n" +
            "bnodes: " + str(self.bnodes) + "\n" +
            "x: (%s, %s)" % (self. min_x, self.max_x) + " "
            "y: (%s, %s)" % (self. min_y, self.max_y)
        )

    def thread_bottom(self, prev):
        def add_prev(p):
            if prev:
                prev.next = p
            return p

        added = False
        if not self.left:
            prev = add_prev(self)
        else:
            prev = self.left.thread_bottom(prev)
        if self.right:
            prev = self.right.thread_bottom(prev)
        return prev


    def print_node(self, level):
        print("{}{}".format(self.spaces[0:level*2], self.value))
        if self.left:
            self.left.print_node(level+1)
        else:
            print("{}None".format(self.spaces[0:(level+1)*2]))
        if self.right:
            self.right.print_node(level+1)
        else:
            print("{}None".format(self.spaces[0:(level+1)*2]))


    def print_bottom(self, level):
        print("in print_bottom")
        n = self
        while n.left:
            n = n.left

        vals = [n.value]
        while n.next:
            n = n.next
            vals.append(n.value)
        
        s1 = string.join(vals, ", ")
        print('bottom:', s1)

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

test.print_node(0)
test.thread_bottom(None)
test.print_bottom(0)
