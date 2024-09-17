class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(lot): 
    if len(lot) == 0:
        return None
    root = Node(lot[0])
    q = [root]
    idx = 1

    while q and idx < len(lot): 
        node = q.pop(0)

        if idx < len(lot) and lot[idx] != 'n':
            node.left = Node(lot[idx]) 
            q.append(node.left) 
        idx += 1

        if idx < len(lot) and lot[idx] != 'n': 
            node.right = Node(lot[idx]) 
            q.append(node.right) 
        idx += 1

    return root

def countLeafNodes(root, cnt):

    if root == None: 
        return [-1] 
    if root.left is None and root.right is None:
        cnt[0] += 1
        return cnt

    if root.left is not None:
        cnt = countLeafNodes(root.left, cnt)
    if root.right is not None:
        cnt = countLeafNodes(root.right, cnt)

    return cnt

levelOrder = list(input().split())
root = constructTree(levelOrder)
print(countLeafNodes(root, [0])[0])