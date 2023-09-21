import math


def solution(arr):
    answer = arr[0]

    #lcm = a * b // math.gcd(a, b)
    for i in arr[1:]:
        answer = answer * i // math.gcd(answer, i)

    print(answer)

solution([2,6,8,14])