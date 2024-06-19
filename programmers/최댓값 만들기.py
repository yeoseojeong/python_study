def solution(numbers):
    answer = 0
    
    max_1=-100
    max_2=-100
    
    
    for i in numbers:
        if max_1<i:
            max_1=i
            
    numbers.remove(int(max_1))
    
    for j in numbers:
        if max_2<j:
            max_2=j
            
    return max_1*max_2
