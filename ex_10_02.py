file = input('Enter file name: ')
handle = open(file)

dic = dict()
for line in handle:
    if line.startswith ('From '):
        short = line.split()
        words = short[5]
        spl = words.split(':')
        fresh = spl[:1]
        for word in fresh:
           dic[word] = dic.get(word, 0) + 1

tmp = list()
for k, v in dic.items():
    newtup = (k, v)
    tmp.append(newtup)
    
last = sorted(tmp) 
for k, v in last:
    print(k,v)