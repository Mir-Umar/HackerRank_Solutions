def fnc(s):
    track_ls = 1
    for i in range(len(s)-1):
        if s[i].isalnum():
            if s[i] == s[i+1]:
                print(s[i])
                break
            else:
                track_ls+=1
        else:
            track_ls+=1
    
    if len(s)==track_ls:
        print(-1)
    


if __name__ == "__main__":
    s = input()
    fnc(s)
