from collections import Counter
if __name__ == '__main__':
    num_shoe = int(input())
    size_shoe_ls = dict(Counter(map(int, input().split())))
    num_customer = int(input())
    customer_ls = []
    for i in range(num_customer):
        cus_tuple = tuple(map(int, input().split()))
        customer_ls.append(cus_tuple)
amount = 0
for i in customer_ls:
    if i[0] in size_shoe_ls.keys() and size_shoe_ls[i[0]]!=0:
        amount+=i[1]
        size_shoe_ls[i[0]]-=1
print(amount)
