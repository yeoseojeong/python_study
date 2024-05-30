def solution(n):
    answer = list(str(n))
    answer.sort()
    length=len(answer)
    sum=0
    
    for i in range(length):
        sum+= int(answer[i])
        
    return sum
