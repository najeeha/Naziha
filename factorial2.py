r = int(input())
factorial = 1
if r < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif r== 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,r+ 1):
       factorial = factorial*i
   print(factorial)
