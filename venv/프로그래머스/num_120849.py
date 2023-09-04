
# 모음 제거

def solution(my_string):

    my_string = my_string.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")

    print(my_string)

solution("nice to meet you")