if __name__ == "__main__":
    m = int(input())
    list_m = set(map(int, input().split()))
    n = int(input())
    list_n = set(map(int, input().split()))
    
intersec = list_m.intersection(list_n)
un = list_m.union(list_n)
for i in sorted(un.difference(intersec)):
    print(i)
