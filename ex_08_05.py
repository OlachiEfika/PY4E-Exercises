fname = input("Enter file name: ")
fh = open(fname)
#file = fh.read()
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    elif line.startswith ('From '):
        #print(line)
        count = count + 1
        #split = line.split()
        ans = line.split()
        short = ans[1:2]
        tab = str(short)
        cut = tab.strip("', ], [")
        print(cut)
    
        #stp = ans.strip('')
        #print(stp)
        #(stp[1:2])


print("There were", count, "lines in the file with From as the first word")


