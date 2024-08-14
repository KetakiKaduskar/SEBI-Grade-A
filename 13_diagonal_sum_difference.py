'''
Input: n (size of the matrix) followed by n*n numbers
Output: Absolute difference Between Diagonal Sums of a Matrix
'''

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

sumDiag1 = sum(matrix[i][i] for i in range(n))
sumDiag2 = sum(matrix[i][n - 1 - i] for i in range(n))
print(abs(sumDiag1 - sumDiag2))