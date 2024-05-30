# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

total = 0
if __name__ == '__main__':
    num_stu = int(input())
    student = namedtuple('student', input())
    for i in range(num_stu):
        ar = input().split()
        stud = student(*ar)
        total= total+int(stud.MARKS)
print(total/num_stu)
