# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

def replace_consecutive_characters(s):
    grouped = groupby(s)
    result = []
    for char, group in grouped:
        count = sum(1 for _ in group)
        result.append((count, char))
        ret = ' '.join(f"({x}, {y})" for x, y in result)
    return ret
    
if __name__ == '__main__':
    string = input()
    output_string = replace_consecutive_characters(string)
    print(output_string)
