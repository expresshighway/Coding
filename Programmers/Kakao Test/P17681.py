def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        location = str(bin(i|j)[2:])
        location = location.rjust(n, '0')
        location = location.replace('1', '#')
        location = location.replace('0', ' ')
        answer.append(location)
    return answer