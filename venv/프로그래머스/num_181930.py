
def solution(a, b, c):
    answer = 0

    if a != b and a != c and b != c:
        answer = a + b + c
    elif a == b and a != c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    elif a != b and a == c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    elif b == c and a != c:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)

    print(answer)

solution(2, 6, 1)
