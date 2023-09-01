
# 짝수의 합

def solution(n) :

    sum = 0
    for num in range(n + 1) :
        if num % 2 == 0 :
            sum += num

    print(sum)

solution(10)