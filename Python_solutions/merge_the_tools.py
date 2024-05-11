from collections import OrderedDict
def merge_the_tools(string,k):
    ret_ls = []
    for i in range(0,len(string),k):
        sub_string = string[i:i+k]
        ret_ls.append(''.join(OrderedDict.fromkeys(sub_string)))
    
    for i in ret_ls:
        print(i)
    return
