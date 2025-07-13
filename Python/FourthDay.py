#Dictionary and set
"""
info ={
    "name":"vandana",
    "cgpa":9.2,
    "subjects": ["python","java","c"],
}
print(type(info))
info["name"]="apna"#over write
print(info)
"""
"""
#nested
student={
    "name":"vandana",
    "subjects":{
        "pys":97,
        "mat":82,

    }

}
# print(student["subjects"]["mat"])
# print(student.keys())
# print(list(student.keys()))
# print(len(student))
# print(student.values())
# print(student.items())
# print(student.get("name"))
print(student.update({"city":"bngr","age":16}))
"""
#SETS IN PYTHON

# nums={1,2,3,4,"hello",2}
# print(type(nums))
# print(len(nums))

# collection={}
# print(type(collection))

#SET METHODS
"""
collection=set()
collection.add(1)
collection.add(3)
collection.add((1,2,3))#tuple can be stored
collection.add(7)

print(collection)

# collection.remove(3)
# print(collection)
# collection.clear()
# print(collection)

"""
"""
collection={"vandana","patil","kssem","cse"}
print(collection.pop())
print(collection)
"""
# set={1,2,3,6,9}
# set2={3,6,0,4}
# print(set.union(set2))
# print(set.intersection(set2))#common values

#Prectice questions
#store words meaning in python dictionary
"""
dict={
    "cat":"a small animal",
    "table":("a piece of table","small table")
}
print(dict)
"""
"""
subjects={
    "python","java","c++","python","javascipt","java",
    "python","java","c++","c"
}
print(subjects)
print(len(subjects))
"""
"""
marks={}
x = int(input("enter phy: "))
marks.update({"phy":x})
x = int(input("enter math: "))
marks.update({"math":x})
x = int(input("enter che: "))
marks.update({"che":x})
print(marks)
"""
# values={9,"9.0"}
# print(values)
values={
    ("float",9.0),
    ("int",9)
}
print(values)

