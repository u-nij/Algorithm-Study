def solution(record):
    answer = []
    
    messages = []
    users = {}
    for r in record:
        inst = r.split()[0]
        userId = r.split()[1]
        
        if (inst != 'Leave') or (userId not in users):
            users[userId] = r.split()[2]

        if inst != 'Change':
            messages.append(inst + ' ' + userId)

    for message in messages:
        userName = users[message.split()[1]]
        if message.split()[0] == 'Enter':
            answer.append(userName + '님이 들어왔습니다.')
        else:
            answer.append(userName + '님이 나갔습니다.')          
        
    return answer