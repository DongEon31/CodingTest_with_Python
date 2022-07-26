## 숫자 문자열과 영단어 - 2021 카카오 채용연계형 인턴십
## https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = s
    # mydict : key - 영단어, value - 숫자
    mydict = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 
              'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
        
    # s 안의 영단어(key = data[0])를 숫자(value = data[1])로 replace
    # replace()는 string에만 적용되므로, data[1]을 str로 cast
    for data in mydict.items():
        answer = answer.replace(data[0], data[1])                    
    
    # answer는 string이므로 int로 cast
    return int(answer)
  
