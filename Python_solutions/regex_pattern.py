# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_substrings_with_vowels(s):
    # Define the regex pattern to match substrings with 2 or more vowels
    pattern = r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])[aeiouAEIOU]{2,}(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])'
    substrings = re.findall(pattern, s)
    return substrings
            
    
if __name__ == "__main__":
    S = input()
    res = find_substrings_with_vowels(S)
    if len(res) == 0:
        print(-1)
    else:
        for i in res:
            print(i)