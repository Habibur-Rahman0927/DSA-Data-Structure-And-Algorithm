def uni_char(s):
    return len(set(s)) == len(s)


print(uni_char('abcdea'))

def uni_char1(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

print(uni_char1('abcde'))