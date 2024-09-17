'''
Your starting point in the maze is marked by the character '#' and the entrance to the library (i.e., end point of the maze) is marked by the character '@', i.e. your program must start from
'#' and end at '@'.

The maze is composed of a rectangular array of cells. Apart from the start (#) and end (@) cells, maze contains solid cells and empty cells. A valid path never passes via a solid cell. The solid cells are marked by 0s and empty cells are marked by 1s. Once on a cell, you can only move to any one of the neighbouring four (i.e., north, east, west, south) cells.

Note: Assume that no path will ever cross itself, i.e., there will be no loops in any path.

input specifiation:
The first line of input will be two integers, R and C, specifying the number of rows and columns.
The next R lines contain C characters each separated by white space, thereby specifying the layout of the maze. It is guaranteed that the maze will contain only one starting and one ending character. Also, it is guaranteed that the maze will contain only one correct path, from the start point to the end point.

output specification:
Your program must output on one line, the number of hops required to reach the end point.

sample i/o:
Sample Input 1
5 10
@ 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1
0 1 0 1 0 1 1 1 0 1
1 1 1 1 0 1 0 0 0 1
# 0 0 1 1 1 1 1 1 1

Sample Output1
24

Sample Input2
5 5
0 0 0 0 0
0 0 0 0 0
0 # @ 0 0
0 0 0 0 0
0 0 0 0 0

Sample Output2
1
'''
def bfs(maze, start, end, rows, cols):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    queue = [(start[0], start[1], 0)]  
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, dist = queue.pop(0)
        
        if (x, y) == end:
            return dist
        
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '0' and not visited[nx][ny]:
                visited[nx][ny] = True  
                queue.append((nx, ny, dist + 1))  

    return -1  

def main():
    R, C = map(int, input().split())

    maze = []
    for _ in range(R):
        maze.append(input().split())

    start = end = None
    for i in range(R):
        for j in range(C):
            if maze[i][j] == '#':
                start = (i, j)
            elif maze[i][j] == '@':
                end = (i, j)

    hops = bfs(maze, start, end, R, C)

    print(hops)

if __name__ == "__main__":
    main()
