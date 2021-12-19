def solution(answers):
    result = []
    first = [1, 2, 3, 4, 5]*len(answers)
    second = [2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(0, len(answers)):
        if (answers[i] == first[i]):
            sum1 = sum1 + 1
        if (answers[i] == second[i]):
            sum2 = sum2 + 1
        if (answers[i] == third[i]):
            sum3 = sum3 + 1
    
    maxValue = max(sum1, sum2, sum3)
    if (maxValue == sum1):
        result.append(1)
    if (maxValue == sum2):
        result.append(2)
    if (maxValue == sum3):
        result.append(3)
    return result