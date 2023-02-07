# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


arr=[]
N = int(input())
for _ in range(N):
    cmd, *args= input().split()
    if cmd=='print':
        print(arr)
    elif cmd=='append':
        arr.append(int(args[0]))
    elif cmd=='insert':
        args=list(map(int,args))
        arr.insert(args[0], args[1])
    elif cmd=='remove':
        arr.remove(int(args[0]))
    elif cmd=='sort':
        arr.sort()
    elif cmd=='pop':
        arr.pop()
    elif cmd=='reverse':
        arr.reverse()
    else:
        raise RuntimeError