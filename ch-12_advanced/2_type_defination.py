# type defination ********
#variable
# n : int = 5
# name : str = "bhavin"

# use to in function ******

# def sum(a:int,b:int) -> int:
#     return a + b

# print(sum(2,4))

# advanced type ***********

from typing import List,Tuple,Any,Union,o

listDate: list[int] = [1,2,3,4,4]

mark : tuple[int] = (1,3,5,6)

name : tuple[any,...] = ("bhavin",123,"fadjk",("bhavin","bhavin hariyani"))

score : dict[str,int] = {"ms":99,"virat":100}

identifier: Union[int, str] = "ID123" 
identifier = 12345  # Also valid
# In Python 3.10 and above, you can use the pipe | operator instead of Union:
identifier: int | str = "ID123"
identifier = 12345