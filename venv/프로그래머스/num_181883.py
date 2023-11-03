
def solution(arr, queries):

    for i in queries:
        increse = [x + 1 for x in arr[i[0]:i[1]+1]]
        arr[i[0]:i[1]+1] = increse

    print(arr)

solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]])