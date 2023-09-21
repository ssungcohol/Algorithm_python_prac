from collections import deque

def solution(people, limit):
    answer = 0

    #최대인원 2명
    #무게제한
    #구명보트를 최대한 적게 이용하는 횟수
    #3시 15분 시작 3시 50분


    people = deque(sorted(people))

    # print(people)

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        else:
            people.pop()
            answer += 1

    if len(people) == 1:
        answer += 1
        # break

    print(answer)

solution([70, 80, 50],100)