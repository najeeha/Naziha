n = int(input())
factorial = 1
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n== 0:
   print(1)
else:
   for i in range(1,n+ 1):
       factorial = factorial*i
   print(factorial)
