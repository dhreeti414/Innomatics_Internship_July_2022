def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        unique=''
        for j in string[i : i+k]:
            if j not in unique:
                unique+=j
        print(unique)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)