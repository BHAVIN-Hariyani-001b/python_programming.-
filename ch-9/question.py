# import this # this modual is print to "zen of python"
# print(this)

# write to poem file ***

# with open("ch-9/poem.txt",'w') as f:
#     f.write(this.s)

# read to poem file ***


# About codecs.decode(text, 'rot_13') ******
# It's used to decode a ROT13-encoded string.
# codecs is a built-in Python module; no installation needed.
# 'rot_13' is a supported text encoding format in Python (for encoding/decoding only).
# 1 ***********

# from codecs import decode  
# with open("ch-9/poem.txt") as f:
#     content = f.read()
#     print(content,end="\n")
#     decoded = decode(content,'rot-13')
#     if "Beautiful" in decoded:
#         print("yes it is present in poem file") 
#     else:
#         print("word is Not present poem file")



# 2
# import random
# def game():
#     print("you are playing the game...")
#     score = random.randint(1,50)

#     #fetch the high score
#     with open("ch-9/highScore.txt") as f:
#         hiScore = f.read()
#         if hiScore != "":
#             hiScore = int(hiScore)
#         else:
#             hiScore = 0
#     print(f"your score {score}")
#     if score > hiScore:
#         with open("ch-9/highScore.txt","w") as f:
#             f.write(str(score))
#     # return score
# game()

# 3
# def tableGenrate(n):
#     table = ""
#     for i in range(1,11):
#        table += f"{n} X {i} = {i*n}\n"

#     with open(f"ch-9/table_print/table_{n}.txt","w") as f:
#             f.write(table)

# for i in range(1,21):
#     tableGenrate(i)


# 4 

# with open("ch-9/file.txt","r") as f:
#     content = f.read()

# contentNew = content.replace("Donkey","######")

# with open("ch-9/file.txt","w") as f:
#     content = f.write(contentNew)

# 5

# words = ["Donkey","bad","gadha"]

# with open("ch-9/file.txt","r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word,("#" * len(word)))

# with open("ch-9/file.txt","w") as f:
#     content = f.write(content)

# 6

# with open("ch-9/log.txt","r") as f:
#     find = f.read()
# if "python" in find:
#     print("Yes python is present in log file")
# else:
#     print("No python is not present in log file")


# 7

# with open("ch-9/log.txt","r") as f:
#     for index,i in enumerate(f.readlines()):
#         if "python" in i:
#             print("Yes python is present in log file")
#             print(f"python word is line number {index + 1}")
#             break
#     else:
#         print("No python is not present in log file")

# 8 
# with open("ch-9/this.txt","r") as f:
#     find = f.read()
# with open("ch-9/this_copy.txt","w") as f:
#     f.write(find)

# 9 

# with open("ch-9/this.txt","r") as f:
#     find1 = f.read()
# with open("ch-9/this_copy.txt","r") as f:
#     find2 = f.read()

# if find1 == find2:
#     print("yes these files are identical")
# else:
#     print("No these files not identical")

# 10
# with open("ch-9/this_copy.txt","w") as f:
#     f.write("")

# 11
# from os import rename
# rename("ch-9/old.txt","ch-9/rename_by_python.txt")

# with open("ch-9/old.txt") as f:
#     content = f.read()
# with open("ch-9/rename_by_python.txt","w") as f:
#     f.write(content)