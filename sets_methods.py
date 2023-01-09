# adding element to a empty set
from re import A


a= set()
print(set(a))
print(type(a))


a.add(4)
a.add(99)

print(a)
# we cannot add list to a set/dictionary as  we can change it afterwards.
a.add((2,3,4,"adarsh"))
print(a)
# treating it as a single element
print(len(a))
# use to print the length
a.remove(99)
print(a)
# use to remove the data items
print(a.pop())
print(a.pop())
# use to give any random data
a.intersection({4,99,44,5,456,43756,8})

