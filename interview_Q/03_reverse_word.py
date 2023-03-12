def rev_word(s):
    words = []
    length = len(s)
    space = [" "]

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start : i])

        i += 1
    return " ".join(reverse(words))

def reverse(lst):
    i = 0            # first item
    j = len(lst)-1   # last item
    while i<j:
        lst[i],lst[j] = lst[j],lst[i]
        i += 1
        j -= 1
    return lst

word = 'Hi Habib, Are you ready to go'
print(rev_word(word))





def rev_word1(s):
    return " ".join(reversed(s.split()))

word = 'Hi Habib, Are you ready to go'
# print(rev_word1(word))

def rev_word2(s):
    return " ".join(s.split()[::-1])

# print(rev_word2(word))

