file = input('Enter file name: ')
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(file)

dic = dict()
for line in handle:
    if line.startswith ('From '):
        short = line.split()
        words = short[1:2]
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        
bigcount = None
bigword = None
for word,count in dic.items():
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword, bigcount)

