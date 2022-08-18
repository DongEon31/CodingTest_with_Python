## 점프와 순간 이동 - Summer/Winter Coding(~2018)
## https://school.programmers.co.kr/learn/courses/30/lessons/12980

# Bottom-Up
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2,n+1):
        if i%2 == 1:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = min(dp[i-1]+1,dp[int(i/2)])
    
    return dp[n]
  
  
# Top-down
def solution(n):
    ans = 0
    while n != 2:
        # n == 1일 때
        if n == 1:
            return 1
        # n이 짝수일 때, 슈트 이용
        elif n % 2 == 0:
            n //= 2
        # n이 홀수일 때, 건전지 소모
        elif n % 2 == 1:
            n -= 1
            ans += 1
    ans += 1
    return ans
  
