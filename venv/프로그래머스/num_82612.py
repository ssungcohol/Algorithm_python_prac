
def solution(price, money, count):
    answer = -1

    sum = 0
    for i in range(1, count + 1):
        sum += i * price

    if (money - sum >= 0):
        answer = 0
    else:
        answer = sum - money


    print(answer)

solution(3,30,4)