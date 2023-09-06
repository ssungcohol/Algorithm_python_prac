
def solution(array, n):
    answer = 0

    for i in range(len(array)):
        if array[i] == n:
            answer += 1

    print(answer)

solution([1, 1, 2, 3, 4, 5],1)