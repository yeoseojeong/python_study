def solution(s):
    answer = ''
    lst = list(s)
    lst.sort()
    lst.reverse()

    for i in lst:
        answer += i

    return answer



