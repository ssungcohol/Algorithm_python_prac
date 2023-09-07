
def solution(n):
    answer = 0

    # s = []
    # for i in str(n):
    #     s.append(i)
    #
    # s.sort(reverse=True)
    #
    # string = ''
    # for i in s:
    #     string += i
    #
    # answer = int(string)
    # ====================================

    #한줄 간단화..
    # s = str(n)
    # s_list = sorted(s, reverse= True)
    answer = int("".join(sorted(str(n), reverse= True)))

    print(answer)

solution(118372)