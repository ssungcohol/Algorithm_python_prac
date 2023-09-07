
def solution(n):

    answer = []

    for i in str(n):
        answer.append(n % 10)
        n = n // 10

    print(answer)


solution(12345)