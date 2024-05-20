from collections import defaultdict
if __name__ == "__main__":
    num_a, num_b = list(map(int, input().split()))
    ls_a, ls_b = [], []
    for _ in range(num_a):
        ls_a.append(input())
    for _ in range(num_b):
        ls_b.append(input())
        
d = defaultdict(list)
for i in range(len(ls_a)):
    d[ls_a[i]].append(i+1)

for i in ls_b:
    if i in d.keys():
        print(' '.join(str(n) for n in d[i]))
    else:
        print(-1)
