
def solution(n):
    ans = 0

    #점프는 이동거리 +1, 배터리 +1
    #순간이동 = 이동거리 * 2

    while n > 0:
        ans += n % 2
        n //= 2

    print(ans)

solution(5)