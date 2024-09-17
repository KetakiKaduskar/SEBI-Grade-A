class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(lot): 
    root = Node(lot[0]) 
    q = [root] 
    idx = 1

    while q and idx < len(lot): 
        node = q.pop(0)

        if idx < len(lot) and lot[idx] != 'n': 
            node.left = Node(lot[idx]) 
            q.append(node.left) 
        idx += 1

        if idx < len(lot) and lot [idx] != 'n': 
            node.right = Node(lot[idx]) 
            q.append(node.right) 
        idx += 1

    return root

def maxNodeLevel(root):
    dic = {}
    q = [root]
    maxNumOfNodesAtLevel = 0 
    level = -1

    while q:
        size = len(q) 
        count = 0 
        level += 1

        while size > 0:
            node = q.pop(0)
            count += 1
            if node.left != None: 
                q.append(node.left)

            if node.right != None: 
                q.append(node.right)

            size -= 1

        if count >= maxNumOfNodesAtLevel:
            maxNumOfNodesAtLevel = count 
            maxLevel = level
            dic[maxLevel] = maxNumOfNodesAtLevel
    
    return {key: val for key, val in dic.items() if val == maxNumOfNodesAtLevel}

levelOrder = list(input().split())
root = constructTree(levelOrder)
print(maxNodeLevel(root))