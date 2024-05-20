from itertools import permutations
def perm(string, k=None):
    if k is None:
        perm_ls = sorted(list(permutations(string, len(string))))
        for i in perm_ls:
            print(''.join(i))
    else:
        perm_ls = sorted(list(permutations(string, k)))
        for i in perm_ls:
            print(''.join(i))

if __name__=='__main__':
    string, k = input().split()
    perm(string, int(k))
