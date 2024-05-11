def minion_game(string):
    # your code goes 
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    # Number of matching sub strings will be the number of char after each char in the given string
    # For example: If S = "Banana", there will be 6 matching sub-strings -- ("B","Ba","Ban","Bana","Banan","Banana")
    
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
