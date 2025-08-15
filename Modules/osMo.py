import os 

# Working with Directories ***********

# print(os.getcwd()) # Get current working directory
# print(os.listdir())     # List files and folders in current directory

# os.chdir("C:/Mingw")  # Change current directory
# print(os.listdir())     # List files and folders in current directory


# Creating and Removing Folders ***************
# os.mkdir("MyDEMO")  # Create a folder
# os.makedirs("a/b/c")  # Create nested folders
# os.rmdir("MyDEMO")   # Remove folder (only if empty)
# os.removedirs("a/b/c")


# File Operations **********
# os.rename("file.txt","file.py") # Rename file/folder
# "" > abc.py # use to cmd create empty file
# "print('HEllo')" > abc.py # use to cmd create 
# os.remove("abc.py") # Delete a file
# os.remove("file.py") # Delete a file

# Path Operations ***********
# print(os.path.exists("osMo.py"))  # Check if file/folder exists
# print(os.path.isfile("osMo.py")) # Is it a file?
# print(os.path.isdir("Modules")) # Is it a folder?

# print(os.path.join("abc","abc.py")) # Join path safely
# print(os.path.basename("abc/to/abc.py")) # Get file name
# print(os.path.dirname("/abc/to/abc.py"))  # Get folder name

# Environment Variables *********
# print(os.environ) #  All environment variables

# os.environ["Modules"] = "E:/PYTHON/repetPython/Modules"
# print(os.environ.get("Modules")) #  Get PATH variable

# Running System Commands *******
os.system("echo Hello")   # Run a shell command
