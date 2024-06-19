def solution(array_d):
    answer = 0
    
    array=sorted(array_d)
    
    for i in array:
        if len(array)%2==0:
            answer=array[(len(array)//2)+1]
        else:
            answer=array[(len(array))//2]
    
    return answer
