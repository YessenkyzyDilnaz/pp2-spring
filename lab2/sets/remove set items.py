#ex1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#ex2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#ex3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

#ex4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

