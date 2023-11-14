
def solution(num_list, n):

    answer = [num_list[idx * n : (idx + 1) * n] for idx in range(len(num_list) // n)]

    print(answer)

solution([1, 2, 3, 4, 5, 6, 7, 8], 2)