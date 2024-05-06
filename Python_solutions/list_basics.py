
N = int(input())
given_ls = []
for i in range(N):
    opt, *values = input().split()
    given_ls.append([opt,list(map(int,values))])
op_ls = []
for item in given_ls:
    if item[0] == 'append':
        op_ls.append(item[1][0])
    elif item[0] == 'insert':
        op_ls.insert(item[1][0],item[1][1])
    elif item[0] == 'remove':
        op_ls.remove(item[1][0])
    elif item[0] == 'sort':
        op_ls = sorted(op_ls)
    elif item[0] =='pop':
        op_ls.pop()
    elif item[0] == 'reverse':
        op_ls = op_ls[::-1]
    elif item[0] == 'print':
        print(op_ls)
    print(op_ls)