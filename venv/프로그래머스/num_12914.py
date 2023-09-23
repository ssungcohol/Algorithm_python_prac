
def solution(n):

    if n < 3:
        answer = n
    else:

        d = [0] * (n + 1)
        d[1] = 1
        d[2] = 2

        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]

        answer = d[i] % 1234567

    print(answer)

solution(4)