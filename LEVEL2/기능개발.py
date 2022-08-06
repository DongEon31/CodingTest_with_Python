## 기능개발 - 스택/큐
## https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    
    while sum(answer) < length:
        complete = 0
        # 각 progress에 speed를 더함
        for i in range(len(progresses)): 
            progresses[i] += speeds[i]
        
        # 앞에서부터 progress가 100 이상인지 check.
        # 앞의 모든 progress가 100 이상이어야 그 뒤의 progress도 배포될 수 있다.
        for idx, progress in enumerate(progresses):
            if complete == idx and progress >= 100:
                complete += 1
        
        # 배포된 progress와 대응되는 speed를 함께 제외시킴
        progresses = progresses[complete:]
        speeds = speeds[complete:]
        
        # 배포된 경우, answer에 추가
        if complete != 0:
            answer.append(complete)
    return answer
    
