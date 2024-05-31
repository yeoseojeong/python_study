def solution(phone_number):
    answer = []
    
    phone_list=list(phone_number)
    
    for i in range(len(phone_number)-4):
        phone_list[i]='*'
        
        
    return ''.join(phone_list)
