def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    kevinScore,stuartScore=0,0
    string_length=len(string)
    for start in range(string_length):
        if string[start] in vowels:
            kevinScore += string_length-start
        else:
            stuartScore += string_length-start
            
    if kevinScore > stuartScore:
        print("Kevin",kevinScore)
    elif kevinScore < stuartScore:
        print("Stuart",stuartScore)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)