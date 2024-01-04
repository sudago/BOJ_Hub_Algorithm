word = input()
for ch in word:
    if ch == ch.lower():
        print(ch.upper(), end="")
    else:
        print(ch.lower(), end="")