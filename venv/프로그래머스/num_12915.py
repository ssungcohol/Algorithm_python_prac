
def solution(strings, n):

    # answer = []
    # new = []
    #
    # for i in range(len(strings)):
    #     new.append(strings[i][n] + strings[i])
    #
    # new.sort()
    #
    # for i in range(len(new)):
    #     cut = new[i]
    #     cut = cut[1:]
    #     answer.append(cut)

    #===============================================

    strings.sort()
    answer = sorted(strings, key=lambda x:x[n])

    print(answer)

solution(["abce", "abcd", "cdx"], 2)