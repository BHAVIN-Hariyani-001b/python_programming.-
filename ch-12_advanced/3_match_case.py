def http_status(status): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: # Default Value
            return "Unknown status" 
 
# Usage 
# print(http_status(200))  # Output: OK 
# print(http_status(404))  # Output: Not Found 
# print(http_status(500))  # Output: Internal Server Error 
# print(http_status(403))  # Output: Unknown status


# Combine Values***
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
# day = 1
# day = 2
day = 7
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")



# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:
# it is check to case match and if statement check and if and case condition are true and value return  
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5  if month == 5:
    print("A weekday in May")
  case _:
    print("No match")