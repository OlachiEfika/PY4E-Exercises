import re
handle = open('mydata.txt')
hand = handle.read()
numlist = list()
for line in hand:
    test = re.findall('[0-9]+',hand)
num = [int(i) for i in test]
#total = sum(num)
print(sum(num))
    
