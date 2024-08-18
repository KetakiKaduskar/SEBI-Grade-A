'''
Input: An integer number
Output: Digit - count
'''

n = input()
numDict = {}
for num in n:
    if num not in numDict and '0' <= num <= '9':
        numDict[num] = 1
    elif '0' <= num <= '9':
        numDict[num] += 1

print("".join(f"{key} - {value}\n" for key, value in numDict.items()))