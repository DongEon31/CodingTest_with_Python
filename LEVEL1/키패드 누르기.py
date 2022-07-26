## 키패드 누르기 - 2020 카카오 인턴십 
## https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    keypad = {1:[0,0], 2:[0,1], 3:[0,2],
             4:[1,0], 5:[1,1], 6:[1,2],
             7:[2,0], 8:[2,1], 9:[2,2],
             '*':[3,0], 0:[3,1], '#':[3,2]}
    left_loc, right_loc = keypad['*'], keypad['#']
    
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left_loc = keypad[number]
        elif number in [3,6,9]:
            answer += 'R'
            right_loc = keypad[number]
            
        else:
            
            if abs(keypad[number][0] - left_loc[0]) + abs(keypad[number][1] - left_loc[1])  > abs(keypad[number][0] - right_loc[0]) + abs(keypad[number][1] - right_loc[1]):
                answer += 'R'
                right_loc = keypad[number] 
            elif abs(keypad[number][0] - left_loc[0]) + abs(keypad[number][1] - left_loc[1]) < abs(keypad[number][0] - right_loc[0]) + abs(keypad[number][1] - right_loc[1]):
                answer += 'L'
                left_loc = keypad[number] 
            
            else:
                if hand == 'left':
                    answer += 'L'
                    left_loc = keypad[number] 
                else:
                    answer += 'R'
                    right_loc = keypad[number] 
    return answer
  
