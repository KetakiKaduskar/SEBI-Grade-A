def ts(s): 
    t = []

    for i, ch in enumerate(s):
        if ch.isalpha():
            nch = chr(((ord(ch.upper()) - ord('A') + 2) % 26) + ord('A')) 
            t.append(nch.lower() if ch.islower() else nch)
        else:
            t.append(ch)

    return ''.join(t)

sent = "hello world!!"
print(ts(sent))