number=int(input("enter the range: "))

print("Prime numbers less than ",number ,"are :")

for num in range(0, number + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
