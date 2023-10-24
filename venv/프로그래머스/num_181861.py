
def solution(arr):
    answer = []

    for i in arr:
        for j in range(i):
            answer.append(i)

    print(answer)

solution([5, 1, 4])