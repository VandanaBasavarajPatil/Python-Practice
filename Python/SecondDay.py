#string and conditional statements
#escape sequence character
# str1="i am vandana.\n from kssem"
# print(str1)
"""
str1="vandana"
print(len(str1))

str2="kssem"
print(len(str2))
final_str=str1+" "+str2
print(final_str)
#indexing
print(str1[3])
#slicing
print(final_str[0:5])

print(str1[:2])#[0:2]
print(final_str[4:])#[4:len(str)]
print(str1[-3:-1])
"""
#string functions
"""
str=" i am a coder."
print(str.endswith("er."))
str=str.capitalize()
print(str)
print(str.replace("a","y"))

print(str.find("i"))
print(str.count("am"))
"""
#WAP to input users first name and print its lenth
"""
name=str(input("enter name:"))
print("length of my name is:",len(name))
"""
#finad occurence of"$" in a string
"""
str="hi am the $vandan $from $kssem"
print(str.count("$"))
"""


#condtional statements
"""
age=21
if(age>=18):
#nesting
   if(age>=80):
      print("cnats")
   else:
    print("driving lisence available")
else:
    print("driving lisence")
"""
    
"""
light="black"
if(light == "red"):
    print("stop")
elif(light == "green"):#if statement flase
    print("go")
elif(light == "blue"):
    print("wait")
else:
    print("no color")#if above all statements are false
"""

#grades of student
"""
marks=int(input("enter marks:"))
if(marks >= 90):
   grade="A"
elif(marks > 80 & marks <= 90):
     grade="B"
elif(marks < 80 & marks > 70):
     grade="c"
else:
    grade="D"
print("grade of student:",grade)
"""

#lets practice
#WAP if user enterd number is even or odd
"""
num=int(input("enter number:"))
if(num % 2 ==0):
    print("even")
else:
    print("odd")
    """

#find the gretest of 3 numbers entered by user
"""
a=int(input("eneter 1 number:"))
b=int(input("eneter 2 number:"))
c=int(input("eneter 3 number:"))
if(a>=b and a>=c):
    print("a")
elif(b>=c):
    print("b")
else:
    print("c")
"""
#If number is multiple of 7 or not
num=int(input("eneter number:"))
if(num%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")