'''
In this problem you have to write a program to check if two given binary trees are
structurally equivalent.
Two trees are structurally equivalent if they are both null or if the left and right children of
one are structurally equivalent to the RESPECTIVE children of the other. In other words,
when you draw the trees on paper, they should LOOK alike (ignoring the values at the
nodes).

Construct a binary search tree with the input in the second line and use this as the basis-
tree. For each of the remaining N-1 lines, construct a binary search tree and compare
against the basis tree for equivalence. If the trees are equivalent, print YES else print
NO. Also print the depth difference between the two trees (ie, depth of the bigger tree
minus the depth of the smaller tree). Both these for a given tree pair must be on one line
separated by a space.
The answers for the different pairs must be on separate lines.

Input:
The input to the program is a number N followed by N lines of input. Each line consists
of a sequence of positive numbers terminated by -1. There will be no duplicate
numbers in any of the lines.

Sample IO:
Input
5
1 3 2 4 -1
4 1 2 3 -1
3 2 1 4 -1
4 3 2 1 -1
1 3 4 2 -1

Output
NO 1
NO 0
NO 1
YES 0
(Note that the depth difference will be zero if the trees are equivalent.)
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def addToBST(root, val):
    if root is None:
        return Node(val)
    if val < root.value:
        root.left = addToBST(root.left, val)
    else:
        root.right = addToBST(root.right, val)
    return root

def convertToBST(vals):
    root = None
    for val in vals:
        if val != -1:
            root = addToBST(root, val)
    return root

def compareTrees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return compareTrees(root1.left, root2.left) and compareTrees(root1.right, root2.right)
    return False

def calcDepth(node):
    if node is None:
        return 0
    return 1 + max(calcDepth(node.left), calcDepth(node.right))

N = int(input().strip())
trees = []

for _ in range(N):
    values = list(map(int, input().strip().split()))
    trees.append(convertToBST(values))

basisRoot = trees[0]

for i in range(1, N):
    if compareTrees(basisRoot, trees[i]):
        print("YES 0")
    else:
        print(f"NO {abs(calcDepth(basisRoot) - calcDepth(trees[i]))}")