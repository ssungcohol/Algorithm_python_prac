
def solution(todo_list, finished):
    answer = []

    for i in range(len(todo_list)):
        if finished[i] is not True:
            answer.append(todo_list[i])

    print(answer)

solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False])