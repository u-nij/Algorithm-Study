# 한 조직원당 한명의 보스
# 보스는 여러명의 조직원으로부터 수익금 받기 가능, 다시 자신의 보스에게
# 수익금 보낼 보스 없을 경우, 최종 보스

# 조직원 아이디 => 최종 보스라면 해당 조직의 조직원 수 구하기(최종 보스 포함)

# 각 조직원들의 보스 p
# 조사하고자 하는 조직원 아이디 담긴 b
# 조직원이 최종 보스일 경우, 조직원수 구해 순서대로 배열에 담아 return

# 조직원 아이디 : 0~p-1 정수형태
# p[i]는 아이디가 i인 조직원의 "보스" 아이디
# -1일 경우, i번 조직원이 해당 조직의 최종 보스
# -1의 개수 = 조직의 개수

p = [2,2,-1,1,5,-1,5]
b = [1, 5]

result = []
num_of_booha = [0 for _ in range(len(p))]

# 조직원의 최종 보스 찾기
def search_boss(id):
    while p[id] != -1:
        id = p[id]
    return id

# 조직원의 수
for i in range(len(p)):
    if p[i] != -1:
        boss = search_boss(p[i])
        num_of_booha[boss] += 1

for i in range(len(b)):
    # 조사하는 조직원이 최종 보스일 경우
    if p[b[i]] == -1:
        result.append(num_of_booha[b[i]]+1)
    # 최종 보스가 아닐 경우
    else:
        result.append(0)

print(result)