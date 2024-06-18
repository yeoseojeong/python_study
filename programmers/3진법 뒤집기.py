def solution(n):
   
    answer = []
    while n != 0:
        answer.append(n % 3)
        n //= 3


    result = 0
    
    for i in range(len(answer)):
        result += answer[i] * (3 ** (len(answer) - 1 - i))
    
    return result



