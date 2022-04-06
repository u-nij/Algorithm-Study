import math

n = int(input())
hp_food = []
for _ in range(n):
    hp_food.append(list(map(int, input().split())))

for hp, food in hp_food:
    live = 0
    while(hp >= 1):
        if food >= 1:
            food -= math.pow(2,int(math.log2(hp))+1) - hp
            hp = math.pow(2,int(math.log2(hp))+1)
        hp //= 2
        live += 1
    print(live)
