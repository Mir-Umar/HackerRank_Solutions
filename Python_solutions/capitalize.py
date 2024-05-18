# Complete the solve function below.
def solve(s):
    s = list(s)
    if s[0].isalpha():
        s[0] = s[0].upper()
    for i in range(1,len(s)-1):
        if s[i] ==' ' and s[i+1].isalpha():
            s[i+1] = s[i+1].upper()
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
