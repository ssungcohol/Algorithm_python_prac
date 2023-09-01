
# 배열 원소의 길이

def solution(strList) :

    # for a in strList:
    #     print(len(a))

    answer = [len(a) for a in strList]
    print(answer)

solution(["We", "are", "the", "world!"])