import re
if __name__ == "__main__":
    lines = int(input())
    inp_str = ""
    for _ in range(lines):
        line = input() + '\n'
        inp_str+=line

ret_str1 = re.sub(r'(?<=\s)&&(?=\s)', 'and', inp_str)
ret_str2 = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', ret_str1)
print(ret_str2)
