def solution(myString, pat):
    answer = 0
    lower_myString = myString.lower()
    lower_pat = pat.lower()

    if lower_pat in lower_myString:
        answer = 1
    return answer
