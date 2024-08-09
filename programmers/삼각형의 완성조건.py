def solution(sides):
    sides_sort = sorted(sides)  
    sides_max = sides_sort[2]   
    sides_sum = sides_sort[0] + sides_sort[1] 

    if sides_sum > sides_max:
        return 1 
    else:
        return 2  
