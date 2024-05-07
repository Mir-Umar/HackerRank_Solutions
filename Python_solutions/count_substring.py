# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count = 0
    ss = string[:len(sub_string)]
    if ss == sub_string:
        count+=1
    ss1 = string[len(sub_string):]
    for i in ss1:
        ss+=i
        ss = ss[1:]
        # print(ss)
        if ss == sub_string:
            count+=1
    return count