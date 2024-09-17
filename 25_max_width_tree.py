class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Pair:
    def __init__(self, node, idx):
        self.node = node
        self.idx = idx

def constructTree(lot):
    root = Node(lot[0])
    idx = 1
    q = [root]

    while q and idx < len(lot): 
        node = q.pop(0)

        if idx < len(lot) and lot[idx] != 'n': 
            node.left = Node(lot[idx]) 
            q.append(node.left)
        idx += 1

        if idx < len (lot) and lot [idx] != 'n': 
            node.right = Node (lot [idx]) 
            q.append(node.right) 
        idx += 1

    return root

def maxWidthOfTree(root):
    q = [Pair(root, 0)]
    maxWidth = 0

    while q:
        size = len(q)
        leftMostIdx= q[0].idx 
        rightMostIdx= q[0].idx

        while size > 0:
            removedPair = q.pop(0) 
            rightMostIdx = removedPair.idx

            if removedPair.node.left != None:
                q.append(Pair(removedPair.node.left, removedPair.idx * 2 + 1))

            if removedPair.node.right != None:
                q.append(Pair(removedPair.node.right, removedPair.idx * 2 + 2))

            size -= 1

        maxwidth = max(maxwidth, rightMostIdx - leftMostIdx + 1)

    return maxWidth

levelOrderTraversal = list(input().split())
root = constructTree(levelOrderTraversal)
print(maxWidthOfTree(root))