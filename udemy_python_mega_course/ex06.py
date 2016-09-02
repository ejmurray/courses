import datetime

file1 = ".\\files\\file1.txt"
file2 = ".\\files\\file2.txt"
file3 = ".\\files\\file3.txt"

now = datetime.datetime.now()
str(now)
with open(file1, "r") as file:
    file1 = file.read()

with open(file2, "r") as file:
    file2 = file.read()

with open(file3, "r") as file:
    file3 = file.read()

with open(".\\files\\" + now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as file:
     file.write(file1 + '\n' + file2 + '\n' + file3 + '\n' )
