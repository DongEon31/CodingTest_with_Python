## 방금그곡 - 2018 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/17683#

def solution(m, musicinfos):
    answer = ''
    answer_list = []
    music_list = [] # music_list[][0 : start / 1 : end / 2 : name / 3 : melody]
    for music in musicinfos:
        music_list.append(music.split(","))
    
    # 각 INFO를 돌면서, 음표 C#D#F#G#A# 소문자로 처리하기. replace('C#','c')
    # end - start를 계산. len(m)보다 짧으면 그 길이만큼 재생.
    # len(m)보다 길면 악보를 두 배로 늘린다. 그리고 end - start까지 찾으면서 m이 나오는지 check.
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('E#','e')
    for music in music_list:
        fixed_melody = music[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('E#','e')
        start_time = 60 * int(music[0].split(':')[0]) + int(music[0].split(':')[1]) 
        end_time = 60 * int(music[1].split(':')[0]) + int(music[1].split(':')[1]) 
        time = end_time - start_time
        if len(m) < len(fixed_melody): # m이 melody보다 짧을 때
            fixed_melody *= 2
            melody = fixed_melody[:time]
        else: # m이 melody보다 길 때
            fixed_melody *= len(m)//len(fixed_melody)  * 2 + 1
            melody = fixed_melody[:time]
            print(melody)
        
        # answer_list 중 우선순위는 재생 시간, 그리고 입력된 순서임. 
        # 입력된 순서는 answer_list에 append되는 순서랑 같음. end-start만 추가로 저장하자. tuple로!    
        if m in melody:
            answer_list.append((music[2],time))
            
    # 없을 경우 (None) 출력       
    if len(answer_list) == 0:
        return '(None)'
    elif len(answer_list) == 1:
        return answer_list[0][0]
    
    # 2개 이상일 경우 우선순위에 따라 선정
    else: 
        max_time = 0
        for answers in answer_list: 
            if max_time < answers[1] : # 가장 긴 음악을 찾는다
                max_time = answers[1]
                song_name = answers[0]
            elif max_time == answers[1]: # 재생 시간이 같으면 먼저 들어온 것이 우선이므로 continue
                continue
        return song_name
      
      
