
def solution(date1, date2):

    print(1 if int("".join(map(str, date1))) < int("".join(map(str, date2))) else 0)

solution([2021, 12, 28], [2021, 12, 29])