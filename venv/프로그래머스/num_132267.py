
def solution(a, b, n):
    answer = 0

    while n >= a:
        etc = 0
        answer += (n // a) * b
        etc = n % a
        n = (n // a) * b + etc

    print(answer)

solution(5, 3, 21)