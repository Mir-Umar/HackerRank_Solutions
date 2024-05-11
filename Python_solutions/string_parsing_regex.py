# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == "__main__":
    string = input()
    k = input()
n = len(string)
count = 0
for i in range(int(n/len(k))):
    ss = re.search(k,string)
    if ss is not None:
        count+=1
        start = ss.start()
        end = ss.end()
        print((ss.start()+(n-len(string)),ss.end()-1+(n-len(string))))
        string= string[ss.start()+1:]
if not count:
    print((-1,-1))
