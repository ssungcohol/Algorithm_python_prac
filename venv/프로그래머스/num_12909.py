
def solution(s):
    answer = True

    if(s[0] == ')' or s[len(s) - 1] == '(') :
        answer = False
    else:
        cnt = 0
        for i in range(len(s)):
            if(s[i] == '('):
                cnt += 1
            else:
                cnt -= 1

            if (cnt < 0):
                answer = False
                break
        if (cnt != 0):
            answer = False

    print(answer)

solution("(()(")