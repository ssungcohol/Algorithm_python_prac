
def solution(array, height):
    answer = 0

    for i in range(len(array)):
        if (array[i] > height):
            answer += 1

    print(answer)

solution([149, 180, 192, 170], 167)