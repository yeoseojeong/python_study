def solution(array, commands):
    answer = []

    for t in range(len(commands)): 
        temp = array[commands[t][0]-1:commands[t][1]] 
        temp.sort() 
        answer.append(temp[commands[t][2] - 1]) 

    return answer
