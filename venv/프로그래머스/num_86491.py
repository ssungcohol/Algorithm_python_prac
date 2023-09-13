
def solution(sizes):
    answer = 0

    # width = 0
    # height = 0
    #
    # for i in range(len(sizes)):
    #     if(sizes[i][0] < sizes[i][1]):
    #         tmp = sizes[i][0]
    #         sizes[i][0] = sizes[i][1]
    #         sizes[i][1] = tmp
    #
    #     if (width < sizes[i][0]):
    #         width = sizes[i][0]
    #     if (height < sizes[i][1]):
    #         height = sizes[i][1]
    #
    # answer = width * height

    # print(answer)

    #==============================================

    print(max(max(x) for x in sizes) * max(min(x) for x in sizes))

solution([[60, 50], [30, 70], [60, 30], [80, 40]])