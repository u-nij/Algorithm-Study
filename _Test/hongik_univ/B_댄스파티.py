dance = []
for i in range(5):
    dance.append(input())

# jump, wait, sit

position = {}
for j in range(5):
    for i in range(len(dance[j])):
        if '.' != dance[j][i]:
            index = dance[1].find(dance[j][i])
            if index != i and (i not in position) and (index not in position) and index != -1:
                position[index] = 'jump' + ' ' + str(i)
                position[i] = 'wait' + ' ' + str(index)


for i in range(len(dance[0])):
    if i in position and position[i].split()[0] == 'wait':
        jump_index = int(i)
        wait_index = int(position[i].split()[1])

        answer = []
        for j in range(5):
            d_list = list(dance[j])
            d_list[jump_index], d_list[wait_index] = d_list[wait_index], d_list[jump_index]
            answer.append("".join(d_list))

for i in range(5):
    print(answer[i])