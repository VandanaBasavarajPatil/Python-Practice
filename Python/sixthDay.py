#FUCTIONS AND RECURSION
"""
def calc_sum(a,b):
    sum = a + b
    print (sum)
    return sum
calc_sum(2,5)

def calc_sum(a,b):
    return a + b
sum = calc_sum(2,7)#func call;arguments

print(sum)
"""
"""
#average of 3 numbers
def calc_avg(a,b,c):
    sum = a + b + c
    avg=sum/2
    print(avg)
    return avg
calc_avg(2,5,6)
"""
"""
print("vandana",end="$")
print("apna")
"""
"""
#write a program to print len of list
cities=["dehli","pune","mumbai","chennai","noida"]
heros=["thor","bheem","chota","spiderman"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heros)
"""
"""
#print the element of the list in single line
cities=["dehli","pune","mumbai","chennai","noida"]
heros=["thor","bheem","chota","spiderman"]
def print_len(list):
    print(len(list))
print(cities[0],end=" ")
print(heros[1])
"""
"""
#find the factorial of n
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)
"""
"""
#write aprogram to convert usd to inr
def converter(usd_val):
    inr_val=usd_val * 83
    print(usd_val,"USD=",inr_val,"INR")
converter(1)
"""

# #Recursion
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(3)

# def fact(n):
#     if(n==10 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(4))

#WRITE THE RECURSION FUN TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n
# sum=calc_sum(5)
# print(sum)






#RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN LIST
def print_list(list,idx=0):
    if(idx==len(list)):
       return
    print(list[idx])
    (print_list(list, idx+1))

fruits=["banana","mango","apple"]
print_list(fruits)