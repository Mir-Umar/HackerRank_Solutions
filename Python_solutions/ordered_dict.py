# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ord_dict = OrderedDict()

if __name__ == '__main__':
    num = int(input())
    for _ in range(num):
        inp_ls = input().split()
        item = ' '.join(inp_ls[:-1])
        price = int(inp_ls[-1])
        if item in ord_dict.keys():
            ord_dict[item]+=price
        else:
            ord_dict[item] = price
        
# print(ord_dict)
for key,value in ord_dict.items():
    print(key,value)
