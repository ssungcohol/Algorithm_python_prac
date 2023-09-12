
def solution(arr):
    answer = []

    for i    in range(len(arr)):
            if i == 0 or arr[i] != arr[i - 1]:
                answer.append(arr[i])


    print(answer)

solution([4,4,4,3,3])