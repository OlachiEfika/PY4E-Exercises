fname = input("Enter file name: ")
fh = open(fname)
file = fh.read()
div = file.split()

list = []
for line in div:
    if line not in list:
           list.append(line)
list.sort()
print(list)
