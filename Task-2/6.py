def average(array):
    # your code goes here
    val=set(array)
    return ("{:.3f}".format(sum(val)/len(val)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)