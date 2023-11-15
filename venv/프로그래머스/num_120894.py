
def solution(numbers):
    answer = ''

    for i in range(len(numbers) - 1):
        check = numbers[i] + numbers[i + 1]
        if check == "ze":
            answer += "0"
        elif check == "on":
            answer += "1"
        elif check == "tw":
            answer += "2"
        elif check == "th":
            answer += "3"
        elif check == "fo":
            answer += "4"
        elif check == "fi":
            answer += "5"
        elif check == "si":
            answer += "6"
        elif check == "se":
            answer += "7"
        elif check == "ei":
            answer += "8"
        elif check == "ni":
            answer += "9"


    print(int(answer))

solution("onetwothreefourfivesixseveneightnine")