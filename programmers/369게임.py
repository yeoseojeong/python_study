def solution(order):
    order_str = str(order)
    
    answer = 0
    
    for char in order_str:
        if char in '369':
            answer += 1
            
    return answer
