
def solution(before, after):
    answer = 0

    print(1 if sorted(before) == sorted(after) else 0)

solution("olleh", "hello")