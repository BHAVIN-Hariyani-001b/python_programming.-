# open() function use to file open 
# syntax :: The open() function takes two parameters; filename, and mode.

# MODE
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

######################################
# f = open("ch-9/demo.txt") # by defualt is "read" mode use
# print(f.read()) # read() method for reading the content of the file:
# f.close() # colse functoin and colose to file but not reqire

######################################
# write mode and use to file write
# str = "Bhavin hariyani"
# f = open("ch-9/writeDemo.txt","w") 
# f.write(str)
# f.close()

######################################
# readline to line by line use to readline function
# f = open("ch-9/readDemo.txt")
# line = f.readline() # readline to return one by one line and string fromate
# # print(type(line)) 
# print(line)

# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)

# line = f.readlines() # readlines to return all text in list formate
# # print(type(line))
# print(line)
# f.close()

######################################
# use to while loop and readline  print to all text

# f = open("ch-9/readDemo.txt")
# line = f.readline()
# while line != "":
#     print(line)
#     line = f.readline()
# f.close()

######################################
# use to apent mode and it is use only apend text in file
# str = "Hi Bhavin! \n"
# f = open("ch-9/apend.txt","a")
# f.write(str)
# f.close()