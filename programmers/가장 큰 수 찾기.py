def solution(array):
    answer = [0, 0]  
    maximum = 0
    index = 0
    
    for i in range(len(array)):
        if array[i] > maximum:
            maximum = array[i]
            index = i
    
    answer[0] = maximum
    answer[1] = index
    return answer
