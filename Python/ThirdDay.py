#List and Tuples
"""
marks=[12.3,13.4,14.5,16.7]
print(marks)
print(type(marks))
print(marks[3])
print(len(marks))
"""
#list slicing
# marks=[12,13,14,16]
# print(marks[1:3])
# print(marks[-1:])

#list slicing
"""
list=[1,2,3,4,5]
print(list.sort())
print(list.append(7))
print(list.sort(reverse=True))
print(list.reverse())
print(list.insert(1,4))
"""
"""
list=[2,1,3]
list.insert(1,5)
print(list)
print(list.sort())
print(list.remove(1))
print(list.count())
"""

#TUPLES
"""
tup=(4,8,2,6)#tup=(4,8,2,6,)
print(type(tup))
print(tup[0])
print(tup[1:2])
"""
#tuple methodsss
"""
tup=(2,4,6,8)
print(tup.index(2))
print(tup.count(2))
"""
#practice questions
#WAT to ask the user to enter names of thire 3 fav movies &srore them in a list
"""
movies=[]
mov1=(input("enter first name:"))
mov2=(input("enter second name:"))
mov3=(input("enter third name:"))
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
"""
"""
movies=[]
movies.append((input("enter first name:")))
movies.append((input("enter secondname:")))
movies.append((input("enter third name:")))
print(movies)
"""

#to check if a list contains a palindrome of elements(use copy() method)
"""
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
   print("palindrom")
else:
   print("not palindrom")
"""

#WAT to count the number of students with the "A" grade with in the following tuple
"""
tup=("C","D","E","A","A","V","A")
print(tup.count("A"))
"""


#strore the above values in a list and sort them from "A" to "D"
list=["C","D","E","A","A","V","A"]
list.sort()
print(list)
