import math


def solution(n, m):

    answer = []

    # answer.append(math.gcd(n,m))
    # answer.append((n * m) // answer[0])

    #================================================

    #GCD
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    #LCM
    for i in range(max(n, m), (n*m)+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    print(answer)

solution(3, 12)