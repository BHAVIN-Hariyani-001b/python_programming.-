def myFunc():
    print("Hello")

# this code is run to this file and use to other and import and not run code in this file and and other import file and import file run your imported file code 

if __name__ == "__main__":
    # if this code directly is executed by running the file its present in 
    print("we are directly running thie code")
    myFunc()
    print(__name__)