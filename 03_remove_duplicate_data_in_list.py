# Question: Complete the script so that it removes duplicate items from the list a .

# a = ["1", 1, "1", 2]
# Expected output: 

#   ['1', 2, 1] 


a = ["1", 1, "1", 2]

# Answer 1: 

print(list(set(a)))

# Explanation 1: 

# We used a set  function to convert the list to a set that would intermediately produce {'1', 1, 2}  with no duplicates because set objects cannot contain duplicates. Then using list  we converted the set back to a list. The drawback here is that the original order of the items is lost. If you need to preserve the order, you may want to use the solution in Answer 2 below.


# Answer 2:

from collections import OrderedDict
print(list(OrderedDict.fromkeys(a)))

# Explanation 2:

# Ordered dictionaries are another data type in Python that, unlike sets and normal dictionaries they preserve the order of the items. Here OrderedDict.fromkeys(a)  would produce a OrderedDict  like [('1', None), (1, None), (2, None)] . Then we would convert that OrderedDict  to a list


# Answer 3:
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

# Explanation 3:

# This is another solution that would preserve the original order. We go through all the original list items and append them to the new list if they have not been appended before. The downside of this is that the operation can take a lot of time if the list as large as we need to access both lists and perform a conditional in each iteration.



print(list(dict.fromkeys(a)))