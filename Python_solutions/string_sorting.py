# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    inp_str = input()
    
lower = [i for i in inp_str if i.islower()]
lower_st = ''.join(sorted(lower))

upper = [i for i in inp_str if i.isupper()]
upper_st = ''.join(sorted(upper))

odd = [j for j in [int(i) for i in inp_str if i.isnumeric()] if j%2!=0]
odd_st = ''.join(str(i) for i in sorted(odd))

even = [j for j in [int(i) for i in inp_str if i.isnumeric()] if j%2==0]
even_st = ''.join(str(i) for i in sorted(even))

print(lower_st+upper_st+odd_st+even_st)
