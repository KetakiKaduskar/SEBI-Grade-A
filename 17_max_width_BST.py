'''
input: 6 2 7 1 4 8 3 5 0
output: 4

input: 4 3 2 1 5 6 7 -1
output: 8
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Pair:
    def __init__(self, node, idx):
        self.node = node
        self.idx = idx

def maxWidthOfTree(root):
    que = []
    maxWidth = 0

    que.append(Pair(root, 0))

    while len(que) != 0:
        size = len(que)
        lm = que[0].idx
        rm = que[0].idx
        while size > 0:
            size -= 1
            rp = que.pop(0)
            rm = rp.idx

            if rp.node.left is not None:
                que.append(Pair(rp.node.left, rp.idx * 2 + 1))
            if rp.node.right is not None:
                que.append(Pair(rp.node.right, rp.idx * 2 + 2))

        maxWidth = max(maxWidth, rm - lm + 1)

    return maxWidth

def addToBST(root, val):
    if root is None:
        return Node(val)
    if val < root.value:
        root.left = addToBST(root.left, val)
    else:
        root.right = addToBST(root.right, val)
    return root

def convertToBST(values):
    root = None
    for val in values:
        root = addToBST(root, val)
    return root

values = list(map(int, input().split()))
values = values[:-1]

root = convertToBST(values)
print(maxWidthOfTree(root))