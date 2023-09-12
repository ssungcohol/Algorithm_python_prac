
def solution(n):
    answer = 0

    s = ''

    while (n > 0):
        s += str(n % 3)
        n = n // 3

    s = int(s, 3)

    print(s)

solution(45)