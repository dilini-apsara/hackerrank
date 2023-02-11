def average(array):
   
    heights=set(array)
    result=(sum(heights))/len(heights)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
