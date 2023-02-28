import sys
from itertools import combinations
from string import ascii_lowercase

n, k = map(int, sys.stdin.readline().split())
words = [] # 남극의 단어들
public = set("antatica") # 공통 알파벳 집합
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(set(word) - public) # 알파벳 중복 제거 및 공통 알파벳 제외

answer = 0

def possible_read(teaching_word):
    temp = 0
    for word in words:
        possible = True
        for w in word:
            if w not in set(teaching_word):
                possible = False
                break
        if possible:
            temp += 1
    return temp


def solution():
    # 가르칠 수 있는 단어 후보 (공통 알파벳 제외)
    teaching_possible = set(combinations(set(ascii_lowercase) - public, k-5))
    answer = 0

    for teaching_word in teaching_possible:
        # 남극의 단어 중 읽을 수 있는 단어의 개수 구하기
        temp = possible_read(teaching_word)
        answer = max(temp, answer)
    
    return answer

if k < 5:
    print(answer)
else:
    print(solution())

# 시간 초과 및 메모리 초과로 로직 변경
# 백트래킹 이용

from itertools import combinations 
import sys
n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
   cnt = 0
   for word in data:
      canRead = 1
      for w in word:
          # 안배웠으니까 못읽는다.
         if learned[ord(w)] == 0:
            canRead = 0
            break
      if canRead == 1:
         cnt += 1
   return cnt

if k >= 5:
   learned = [0] * 123
   for x in first_word:
      learned[ord(x)] = 1

   # 남은 알파벳 중에서 k-5개를 선택해본다.
   for teach in list(combinations(remain_alphabet, k-5)):
      for t in teach:
         learned[ord(t)] = 1
      cnt = countReadableWords(data, learned)

      if cnt > answer:
         answer = cnt
      for t in teach:
         learned[ord(t)] = 0
   print(answer)
else:
   print(0)