'''
Input: n (indicating the number of binary numbers) followed by n binary numbers
Output: Decimal number
'''

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input(), 2))

print(sum(nums))