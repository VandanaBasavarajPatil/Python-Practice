#LOOPS IN PYTHON

#While Condition
"""
count=1
while count<=5:
    print("hello",count)
    count+=1
    """
#print numbers from 1 to 5
"""
i = 1
while i<=20:
    print(i)
    i += 1

i =5
while i>=1:
    print(i)
    i-=1
    """

#PRACTICE PROBLEMS FOR WHILE LOOP
#1.print numbers from 1 to 100
"""
i=1
while i<=100:
    print(i)
    i+=1

#2.print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i=i-1
"""
#print the multiflication table of n
"""
i=1
n=int(input("enter number:"))
while i<=10:
    print(n*i)
    i+=1
    """
#3.print the element of the following list:[1,4,9,16,25,36,49,64,81,100]
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
   print(nums[idx])  #nums[0],nums[1]....
   idx += 1
"""

#4.serch for a number in this tuple[1,4,9,16,25,36,49,64,81,100]
"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i <len(nums):
   if(nums[i] == x):
      print("fonud at idx",i)
i += 1
"""
#Break and continue
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i <len(nums):
   if(nums[i] == x):
      break
      print("fonud at idx",i)
i += 1

#
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i <len(nums):
   if(nums[i] == x):
      continue
      print("fonud at idx",i)
i += 1

#FOR LOOPs
"""
list=[1,2,3]
for el in list:
   print(el)

tup=(1,2,4,6)
for num in tup:
   print(tup)
"""
"""
str="vandana"
for char in str:
   print(char)
else:
   print("end")
"""
"""
#practice problems
#1.print the elments of the list
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for ele in nums:
   print(ele)
#2.search for a number x in 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49)
x = 49
i=0
for ele in nums:
   if(ele == 49):
     print("x found",i)
     break
     i+=1
"""
#range() 
print(range(5))

for i in range(5):
   print(i)

for i in range(1,5):
   print(i)

for i in range(2,10,2):
   print(i)

for i in range(2,100,2):
   print(i)

#using for and range()
#1.print numbers from 1to 100

for i in range(101):
   print(i)

#1.print numbers from 100 to 1
for i in range(100,0,-1):
   print(i)

#print multifliaction table of n
n=int(input("enter number:"))
for i in range(1,11):
   print(n * i)

#pass stetements
for i in range(5):
   pass
   if i > 5:
      pass
print("statement")

#find the some of n numbers(while)
n=5
sum=0
for i in range(1,n+1):
   sum+=i
   print("total sum is:",sum)



n=7
sum=0
i = 1
while i<= n:
   sum+=i
   i +=1
   print("total sum is:",sum)

#find the factorial of first n numbers
n=5
fact=0
i=1
while i <= n:
   fact *= i
   i +=1
print("factorial:",fact)
