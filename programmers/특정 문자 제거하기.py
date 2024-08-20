def solution(my_string, letter):
    my_string = list(my_string)
    i = 0
    while i < len(my_string):
        if my_string[i] == letter:
            my_string.pop(i)
        else:
            i += 1
    
    return ''.join(my_string)
