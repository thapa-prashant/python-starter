# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1)
list1=list2
print(list2)
print(id(list1))
list1

name="ram"
print(f"my name is {name}")