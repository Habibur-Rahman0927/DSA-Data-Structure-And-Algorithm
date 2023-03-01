# get average number of input

total = 0
count = 0

# while (True):
#     inp = input("Enter a number: ")
#     if inp == 'done': break
#     value = float(inp)
#     total += value
#     count += 1
#     average = total / count

# print(average)


# number_list = []

# while (True):
#     inp = input("Enter a Number: ")
#     if inp == 'done': break
#     number_list.append(float(inp))

# average = sum(number_list)/len(number_list)
# print(average)


num_days = int(input('How many day\'s temperature? '))
temp_list = []

for i in range(1, num_days+1):
    next_days = int(input("Day {0} high temp: ".format(i)))
    temp_list.append(next_days)


avg = round(sum(temp_list)/num_days, 2)
print("\nAverage = {}".format(avg))