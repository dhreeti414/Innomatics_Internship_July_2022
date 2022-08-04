if __name__ == '__main__':
    records=[]
    score_lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        score_lst.append(score)
    second_lowest=sorted(set(score_lst))[1]
    for name,score in sorted(records):
        if(score==second_lowest):
            print(name)
