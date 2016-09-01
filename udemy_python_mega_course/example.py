import datetime

r"""
This script creates an empty file.
'\n' will not be treated as a special character because of the 'r' in first line
"""

filename=datetime.datetime.now()

#Create empty file
def create_file():
   """This function creates an empty file"""
   with open(filename.strftime("%Y%m%d-%H%M%S")+".txt", "w") as file:
      file.write("") #writing empty string
      