'''
Input:
The first line will contain 2 natural numbers, N and M, separated by a blank space. N
indicated the number of departments in the university and M indicates the number of
pairs of departments where the cables can be laid. The following M lines will specify the
distances between M pairs of departments as
dept1 dept2 distance
Assume that the given distances between each pairs
of departments will be unique and these M lines will contain atleast one pair for each
department.

Output:
The first line of the output will be names of the departments as they are included in the
solution separated by blank space. If two or more departments are included at a time
then their names should be printed in the alphabetic order. The next line will be the
minimum length of cable required to form the intranet, terminated with a new line
character.

Sample IO:
Input
7 10
physics chemistry 8
biology physics 9
biology office 15
chemistry office 4
chemistry sanskrit 5
sanskrit office 7
english office 16
english sanskrit 19
english cs 12
sanskrit cs 6

Output
chemistry office sanskrit cs physics biology english
44
'''

class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt

class Pair:
    def __init__(self, v, av, wt):
        self.v = v
        self.av = av
        self.wt = wt

class priorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)
    
    def remove(self):
        self.queue = sorted(self.queue, key=lambda x:x.wt)
        return self.queue.pop(0)

def prims():
    solution = []
    minLength = 0

    while pq.size() > 0:
        rem = pq.remove()

        if visited[rem.v]:
            continue     
        visited[rem.v] = True

        solution.append(rem.v)
        minLength += rem.wt

        for e in graph[rem.v]:
            if not visited[e.nbr]:
                pq.add(Pair(e.nbr, rem.v, e.wt))

    return (solution, minLength)

def addValue(key, value):
    if key not in graph:
        graph[key] = []
    graph[key].append(value)


graph = {}
pq = priorityQueue()

n, m = map(int, input().strip().split())
for _ in range(m):
    dest1, dest2, wt = input().strip().split()
    wt = int(wt)
    addValue(dest1, Edge(dest1, dest2, wt))
    addValue(dest2, Edge(dest2, dest1, wt))

keys = list(graph.keys())
pq.add(Pair(min(keys[0], keys[1]), None, 0))
visited = {key:False for key in keys}
network, wire = prims()

print(" ".join(network))
print(wire)