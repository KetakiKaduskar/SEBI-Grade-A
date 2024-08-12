'''
Input:
Words, numbers, special characters separated by space/tab/newlines , Input is terminated as
word “endpara”,
Note: Assume that endpara will never be the part of snippet.

Output:
Print the missing Alphabets in the paragraph in the ascending order
in CAPITAL separated by space.
If none of the alphabet is missing, print “NONE”.
'''

allAlpha = set("abcdefghijklmnopqrstuvwxyz")
para = []
while True:
    line = input()
    if 'endpara' in line:
        line = line.replace("endpara", "")
        para.append(line.lower())
        break
    
    para.append(line.lower())

paraString = "".join(para)
alphaPara = set(char for char in paraString if 'a' <= char and char <= 'z')
missingAlpha = allAlpha - alphaPara

if len(missingAlpha):
    print(" ".join(sorted(list(missingAlpha))).upper())
else:
    print("NONE")