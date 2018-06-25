
class Node(object):
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

    # print tree in breadth-first order
    def printTree(self):
        queue = [self]

        level = 1
        num_elements = 1
        row = []
        has_value = False
        while len(queue) > 0:
            n = queue.pop(0)
            if n is not None:
                has_value = True
                queue.append(n.left)
                queue.append(n.right)
            else:
                queue.append(None)
                queue.append(None)
            row.append(n.val if n else '-')
            if len(row) == num_elements:
                if not has_value:
                    break
                print(row)
                row = []
                num_elements *= 2
                has_value = False

    @staticmethod
    def getrows(n, rows, r):
        if n is None:
            return
        if r not in rows:
            rows[r] = []
        rows[r].append(n.val)
        Node.getrows(n.left, rows, r+1)
        Node.getrows(n.right, rows, r+1)

    @staticmethod
    def getcolumns(n, cols, c):
        if n is None:
            return
        if c not in cols:
            cols[c] = []
        cols[c].append(n.val)
        Node.getcolumns(n.left, cols, c-1)
        Node.getcolumns(n.right, cols, c+1)

    def getleft(self):
        rows = {}
        Node.getrows(self, rows, 0)
        return [row[0] for row in rows.values()]

    def getright(self):
        rows = {}
        Node.getrows(self, rows, 0)
        return [row.pop() for row in rows.values()]
    
    def gettop(self):
        cols = {}
        Node.getcolumns(self, cols, 0)
        return [col[0] for col in cols.values()]

    def getbottom(self):
        cols = {}
        Node.getcolumns(self, cols, 0)
        return [col.pop() for col in cols.values()]


            
t = Node(1,
    Node(2,
        Node(4),
        Node(5)
    ),
    Node(3,
        None,
        Node(6,
            Node(7),
            None)
    )
)
t.printTree()
print("left:", t.getleft())
print("right:", t.getright())
print("top:", t.gettop())
print("bottom:", t.getbottom())



          
