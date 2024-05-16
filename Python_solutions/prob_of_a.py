from itertools import combinations
if __name__ == '__main__':
    num = int(input())
    string = input().replace(' ', '')
    choose = int(input())
    
fav = 0
total_com = list(combinations(list(range(len(string))), choose))
ind_a = [i for i, char in enumerate(string) if char=="a"]
for i in total_com:
    if any(element in list(i) for element in ind_a):
        fav+=1
        
print('{:.3f}'.format(fav/len(total_com)))
