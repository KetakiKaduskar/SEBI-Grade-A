def compareStrings(a, b):
    if a == b:
        return f"{a} = {b}"
    elif a in b:
        return f"{a} < {b}"
    elif b in a:
        return f"{a} > {b}"
    else:
        return f"{a} != {b}"

a = input()
b = input()
print(compareStrings(a, b))