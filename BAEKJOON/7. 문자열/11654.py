text = input()

if (text >= 'A' and text <= 'Z') or (text >= 'a' and text <= 'z'):
    print(ord(text))
elif text >= '0' and text <= '9':
    print(ord(text))