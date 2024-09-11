def solution(my_string, indices):
    my_list = list(my_string)
    
    indices = sorted(indices, reverse=True)
    
    for index in indices:
        if 0 <= index < len(my_list):
            my_list.pop(index)
    
    return ''.join(my_list)
