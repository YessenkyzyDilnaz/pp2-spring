#ex1
def greeting(name):
  print("Hello, " + name)

#ex2
import mymodule

mymodule.greeting("Jonathan")

#ex3
import mymodule

a = mymodule.person1["age"]
print(a)

#ex4
import mymodule as mx

a = mx.person1["age"]
print(a)

#ex5
import platform

x = platform.system()
print(x)

#ex6
import platform

x = dir(platform)
print(x)

#ex7
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#ex8
from mymodule import person1

print (person1["age"])