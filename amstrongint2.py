lower,upper = (input( )).split()
a=int(lower)
b=int(upper)
for num in range(a, b):

   
   order = len(str(num))
    

   sum = 0

  
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
