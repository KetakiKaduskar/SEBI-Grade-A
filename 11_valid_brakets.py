'''
Input:
First line of the input consists of an integer N, followed by N number of strings with each string
is on a separate line.

Output:
For each input string, print “MISSMATCH” if the nesting of brackets are not matching. "TOO
MANY OPENING" if more opening brackets then the closing. "TOO MANY CLOSING" if
more closing brackets than the opening brackets. Else if everything is fine print "VALID".
'''

def check_brackets(string):
    stack = []
    charList = [char for char in string if char in [')', '(', ']', '[', '}', '{']]
    string = "".join(charList)
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(bracket_map.values())
    closing_brackets = set(bracket_map.keys())
    missmatch = 0
    putInStack = 0
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
            putInStack += 1
        elif char in closing_brackets:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                missmatch = 1
    
    if float(putInStack) == len(string)/2:
        if missmatch:
            return "MISMATCH"
        else:
            return "VALID"
    elif float(putInStack) < len(string)/2:
        if len(stack) == 0:
            return "TOO MANY CLOSING"
        else:
            return "MISMATCH"
    else:
        if missmatch:
            return "MISMATCH"
        else:
            return "TOO MANY OPENING"
    

# Input
N = int(input().strip())
results = []
for _ in range(N):
    input_string = input().strip()
    results.append(check_brackets(input_string))

# Output
for result in results:
    print(result)