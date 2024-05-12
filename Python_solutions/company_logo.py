from collections import Counter
mydict = dict(Counter(''.join(sorted(st))))
vv = sorted(mydict.items(), key=lambda item:(-item[1],item[0])) # adding a - before the item[1] will reverse the order
for ch,value in vv:
    print(ch,value)
