from collections import deque
dq = deque()
if __name__ == "__main__":
    num = int(input())
    for _ in range(num):
        inp_ls = input().split()
        if inp_ls[0] in ['append', 'appendleft']:
            getattr(dq, inp_ls[0])(inp_ls[1])
        elif inp_ls[0] in ['pop']:
            dq.pop()
        elif inp_ls[0] in ['popleft']:
            dq.popleft()
print(' '.join(list(dq)))
