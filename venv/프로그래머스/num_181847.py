
def solution(n_str):

    cnt = 0
    for i in n_str:
        if i == '0':
            cnt += 1
        else:
            break

    print(n_str.replace('0', '', cnt))

solution("0010")