
def solution(t, p):
    answer = 0

    stn = int(p)

    for i in range(0,len(t) - len(p) + 1):
        s = int(t[i:i+len(p)])

        if (stn >= s):
            answer += 1

    print(answer)

solution("3141592"	, "271")