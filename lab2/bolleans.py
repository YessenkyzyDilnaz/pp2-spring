#ex1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#ex2
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#ex3
print(bool("Hello"))
print(bool(15))

#ex4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#ex5
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#ex6
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#ex7
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

#ex8
def myFunction() :
  return True
print(myFunction())

#ex9
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

#ex10
x = 200
print(isinstance(x, int))

#ex11
print(10 > 9)
#True

#ex12
print(10 == 9)
#False

#ex13
print(10 < 9)
#False

#ex14
print(bool("abc"))
#True

#ex15
print(bool(0))
#False

