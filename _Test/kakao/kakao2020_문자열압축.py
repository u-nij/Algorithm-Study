def solution(s):
    answer = len(s)
    
    for idxLen in range(1, len(s)):        
        compressed = ""
        idxStr = s[0:idxLen]
        tmp = idxStr
        tmpNum = 1
                
        for i in range(idxLen, len(s), idxLen):            
            if i+idxLen >= len(s):
                idxStr = s[i:len(s)]
                
                if tmp == idxStr:
                    compressed += str(tmpNum+1) + idxStr
                else:
                    if tmpNum != 1:
                        compressed += str(tmpNum)
                    compressed += tmp + idxStr
                break
            else:
                idxStr = s[i:i+idxLen]
                
            if tmp != idxStr:
                if tmpNum != 1:
                    compressed += str(tmpNum)
                compressed += tmp
                tmpNum =  1
                tmp = idxStr
            else:
                tmpNum += 1

        # 길이 계산
        if answer >= len(compressed):
            answer = len(compressed)
            
    return answer