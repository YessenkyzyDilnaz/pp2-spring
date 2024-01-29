#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

#ex2
for x in "banana":
  print(x)

#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex6
for x in range(6):
  print(x)

#ex7
for x in range(2, 6):
  print(x)

#ex8
for x in range(2, 30, 3):
  print(x)

#ex9
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#ex10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#ex11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#ex12
for x in [0, 1, 2]:
  pass

#ex1
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#ex2
  i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex4
  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")