# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

pos_hap = 0
neg_hap = 0
my_dict = dict(Counter(arr))
A_dict = dict(Counter(A))
B_dict = dict(Counter(B))
for i in A_dict.keys():
    if i in my_dict.keys():
        pos_hap+=my_dict[i]
for i in B_dict.keys():
    if i in my_dict.keys():
        neg_hap-=my_dict[i]
print(pos_hap+neg_hap)
