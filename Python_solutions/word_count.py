# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ =='__main__':
    num = int(input())
    word_ls = []
    for i in range(num):
        word_ls.append((input()))
        
my_dict = dict(Counter(word_ls))
print(len(my_dict.keys()))
print(' '.join(map(str, list(my_dict.values()))))
