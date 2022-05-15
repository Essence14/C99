file= input("enter the file name ")
file= open(file)
# print(file)
# f=file.read()
# print(f)
f=file.readlines()
for line in f:
    print(line)