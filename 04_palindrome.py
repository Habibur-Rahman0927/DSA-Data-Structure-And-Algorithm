s = input("Enter the value: ")
reverse = s[::-1]

if reverse == s:
    print("Value Is palindrome")
else:
    print("Value Is Not palindrome")
print(reverse)

x = 121
temp = x
rev = 0
while (x > 0):
    # dig = x % 10
    rev = rev*10+x % 10
    x = x//10  # remove last number
if temp == rev:
    print(True)
else:
    print(False)

# print(121%10)
# print(0*10+1)
# print(121//10)
