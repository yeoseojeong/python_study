def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    total=0
    
    for i in numbers:
        if i in answer:
            answer.remove(i)
            
            
    total=sum(answer)
    return total
