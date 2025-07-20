
# df=open("demo.txt","r")
# data=df.read()
# print(data)
# print(type(data))
# # df.close()


# line2=df.read()
# print(line2)
# # df.close()

# df=open("demo.txt","a")
# df.write("the name is ")
# df.close()


# import os
# os.remove("demo.txt")

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using java.\nI like programming in java.")


word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("word") != -1):
       print("found")
    else:
       print("Not Found")

def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
      data=f.read()
      if(data.find("word") != -1):
         print("found")
      else:
         print("Not Found")
check_for_word()


def check_for_line():
   word="learning"
   data=True
   line_no=1
   with open("practice.txt","r") as f:
      while data:
         data=f.readline()
         if(word in data):
            print(line_no)
            return
         line_no += 1

   return -1


with open("practice.txt","r") as f:
   data=f.read()
   print(data)

   num=""

for i in range(len(data)):
    if(data[i]==","):
        print(num)
    else:
        num+=data[i]
      
         
