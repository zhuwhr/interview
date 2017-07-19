def decrypt(word):
    step = 1
    res = ''

    for ch in word:
        ascii_val = ord(ch) - step

        while ascii_val < ord('a'):
            ascii_val += 26

        res += chr(ascii_val)
        step += ascii_val

    return res

print(decrypt('dnotq'))
