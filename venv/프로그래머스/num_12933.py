
def solution(n):
    answer = 0

    s = []
    for i in str(n):
        s.append(i)

    s.sort(reverse=True)

    string = ''
    for i in s:
        string += i

    answer = int(string)

    print(answer)

solution(118372)