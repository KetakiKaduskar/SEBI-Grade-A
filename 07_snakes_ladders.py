'''
Snakes and ladders is a very popular game. It's a 10x10 maze, with cells numbered
from 0 to 99, the player closest
to cell 99 in number is the winner.If there is another snake (or ladder) waiting at the tail of a snake, a player slide down (or
climb up) that second snake (or ladder), and so on as required.

Input:
The first line of input will contain a single integer N, stating the number of snakes
and ladders.
Next N lines each will contain a pair of integers. Each pair will describe either a
snake or ladder by its start cell and an end cell. For example, for a snake, start
cell will be higher than end cell. Refer to the first sample input case which
describes the board in the figure above.
Following line of input has a single integer D, indicating the number of moves
(dice throws) made by both players A and B.
Last line contains D integers, each indicating a dice throw, alternately made by A
and B. First throw is made by player A. Each dice throw is an integer between 1
to 6.

Output:

Your program should output the name of the winner (A or B) followed by the players
position
at the end of game, with a single space in between.

Sample IO
Input:
2
26 87
96 13
18
4 1 3 2 6 3 6 3 2 4 4 2 1 1 5 2 4 6

Output:
B 24

Input:
3
13 98
98 0
6 13
10
5 1 3 3 1 1 4 1 6 1

Output:
B 1
'''

def findFinalPos(diceVals, starts, ends):
    initPos = 0
    for i in range(len(diceVals)):
        if initPos + int(diceVals[i]) < 100:
            initPos += int(diceVals[i])
        while initPos in starts:
            initPos = ends[starts.index(initPos)]
    return initPos

N = int(input().strip())
starts = []
ends = []

for _ in range(N):
    tup = input().strip().split()
    starts.append(int(tup[0]))
    ends.append(int(tup[1]))

D = int(input().strip())
throws = input().strip().split()

AThrows = []
BThrows = []

for i in range(D):
    if i % 2 == 0:
        AThrows.append(throws[i])
    else:
        BThrows.append(throws[i])

AFinalPos = findFinalPos(AThrows, starts, ends)
BFinalPos = findFinalPos(BThrows, starts, ends)

if AFinalPos > BFinalPos and AFinalPos < 100 and BFinalPos < 100:
    print(f"A {AFinalPos}")
else:
    print(f"B {BFinalPos} A {AFinalPos}")