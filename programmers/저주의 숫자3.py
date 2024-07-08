def solution(n):
    answer = 0
    no_3=[]
    for i in range(n*3):
        if not '3' in str(i) and i % 3 != 0:
            no_3.append(int(i))
    return no_3[n-1]
