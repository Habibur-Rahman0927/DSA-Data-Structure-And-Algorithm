# reverse Solution

def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng) - 1 ]+ reverse(strng[0: len(strng) - 1])
    # return reverse(strng[1:]) + strng[0]

print(reverse('python'))

letters = 'abcdefghijklmnopqrstuvwxyz'
backards = letters[::-1]
print(backards)