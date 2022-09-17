## H-Index
## https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = [0]
    new_citations = sorted(citations, reverse=True)
    for i in range(len(new_citations)):
        if i+1 == len(new_citations):
            if new_citations[i] >= i+1:
                answer.append(i+1)
        else:
            if new_citations[i] >= i+1 and new_citations[i+1] <= i+1:
                answer.append(i+1)
    return max(answer)
  
  
