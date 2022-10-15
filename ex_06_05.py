text = "X-DSPAM-Confidence:    0.8475"
#print(text[22:29])
find = text.find('0.')
#find = text.find('5')
#print(find)
slice = text[23:29]
#print(slice)
ans = float(slice)
print(ans)