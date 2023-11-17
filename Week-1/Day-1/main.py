print("hello python")

#data types
a = 10                           #integer
name = "sai"                     #string
present = True                   #boolean
float = 3.14                     #float
list = ["a", "b", "c", "d"]      #list
tuple = ("a", "b", "c", "d")     #tuple
set = {"a", "b", "c", "d"}       #set
dict = {"a": 1, "b": 2}          #dictionary

#for loop
for i in range(10):
    print(i)

#while loop
i = 0
while i < 10:
  print(i)
  i += 1

#if statement
if i > 10:
  print("i is greater than 10")

#function

def findAlphabet(a):
  for i in list:
    if i==a:
      ans = True
    else:
      ans = False
      return ans


print(findAlphabet("f"))