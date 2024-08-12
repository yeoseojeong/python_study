def solution(arr, delete_list):
   
    delete_set = set(delete_list)
    
   
    answer = []
    for item in arr:
        if item not in delete_set:
            answer.append(item)
    
    return answer
