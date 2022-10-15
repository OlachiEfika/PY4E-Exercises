fname = input('Enter file name: ')
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        count = count + 1
        ans = line[20:27]
        #ans = print(line[20:27])
        total = total + float(ans)
print("Average spam confidence:",total/count)
#ans = final/count
#print(ans)
#print(final)
#final = ans/count
#print(final)




