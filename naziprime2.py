a,b=input().split()
m = int(a)
n = int(b)
 
 
aaaa=""
 
for num in range(m,n):
 
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           aaaa = aaaa + str(num)+' ' 
 
print(aaaa.rstrip())
