# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    ret = ''
    for i in s:
        if i.upper() == i:
            ret+=i.lower()
        else:
            ret+=i.upper()
    return ret

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)