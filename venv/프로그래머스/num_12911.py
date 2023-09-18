
def solution(n):
    answer = 0

    check = ''
    check = str(bin(n)).count("1")

    for i in range(n+1, 1000000):
        b2 = ''
        b2 = str(bin(i)).count("1")
        if(check == b2):
            answer = i
            break

    print(answer)

solution(78)