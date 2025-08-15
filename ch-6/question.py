# 1 find the big number in four number

# a1 = int(input("Enter number 1 :"))
# a2 = int(input("Enter number 2 :"))
# a3 = int(input("Enter number 3 :"))
# a4 = int(input("Enter number 4 :"))

# if a1 > a2 and a1 > a3 and a1 > a4:
#     print(f"a1 is big number : {a1}")
# elif a2 > a1 and a2 > a3 and a2 > a4:
#     print(f"a2 is big number : {a2}")
# elif a3 > a1 and a3 > a2 and a3 > a4:
#     print(f"a3 is big number : {a3}")
# else:
#     print(f"a4 is big number : {a4}")

# OR

# listData = [int(input("Enter your number : ")) for i in range(4)]
# print(max(listData))

# 2 

# marks1 = int(input("Enter Marks 1 : "))
# marks2 = int(input("Enter Marks 2 : "))
# marks3 = int(input("Enter Marks 3 : "))

# total_marks = marks1 + marks2 + marks3
# persentage = total_marks / 3

# markAll =  marks1 >= 33 and marks2 >= 33 and marks3 >= 33
# # print(markAll)

# if persentage >= 40 and markAll:
#     print(f"You pass and your Mark : {total_marks} and Persentage : {persentage}")
# elif persentage < 40 and persentage >= 32 and  markAll:
#     print(f"You pass and your Mark : {total_marks} and Persentage : {persentage}")
# else:
#     print(f"You failed and your Mark : {total_marks} and Persentage : {persentage}")



# span = ["Make a lot of money", "buy now", "subscribe this", "click this"]
# mesg = input("Enter meassage : ")

# found = False
# for keyword in span:
#     if keyword.lower() in mesg.lower():
#         print(f"Your message is 'span', '{keyword}' keywork is not valid use to in message")
#         found = True

# if not found:
#     print("Messange is valid")


    
# 4 

# userName =  input("Enter your use name : ")
# if len(userName) < 10:
#     print("user name is valid")
# else: 
#     print("user name is not valid")

# short if else use

# print("user name is valid") if len(userName) < 10 else print("user name is not valid")

# 5

# nameList = ["bhavin","anand","harry","sagar","hemal"]

# name = input("Enter your name : ").lower()
# if name in nameList:
#     print("Name is in list")
# else: 
#     print("Name is not in list")


# 6

# mark = int(input("Enter your mark : "))
# if mark <= 100 and mark > 90:
#     print("Ex")
# elif mark <= 90 and mark > 80:
#     print("A")
# elif mark <= 80 and mark > 70:
#     print("B")
# elif mark <= 70 and mark > 60:
#     print("C")
# elif mark <= 60 and mark > 50:
#     print("D")
# else:
#     print("F")

# 7 

# post = input("Enter the post : ").lower()
# if "Bhavin".lower() in post:
#     print("This post is ask about bhavin")
# else:
#     print("This post not ask about bhavin")