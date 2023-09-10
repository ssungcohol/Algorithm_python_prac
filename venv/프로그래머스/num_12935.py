
def solution(arr):

    if len(arr) == 1:
        return [-1]

    arr.remove(min(arr))

    print(arr)

solution([4,3,2,1])