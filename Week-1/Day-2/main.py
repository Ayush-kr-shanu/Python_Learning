#  trying to solve the problem on python language

def add_two_number(a,b):
  return a+b

def subtract_two_number(a,b):
  return a-b

# find the sum of odd number which is equal to or leass than N
def sum_of_odd_number(N):
  sum = 0
  for i in range(1,N+1):
    if i%2 == 1:
      sum += i
  return sum

def sumOfOddNumber (n):
  sum=0
  for i in range(n+1):
    if i%2 !=0:
      sum += i
  return sum

print(sumOfOddNumber(5))
print(sum_of_odd_number(5))