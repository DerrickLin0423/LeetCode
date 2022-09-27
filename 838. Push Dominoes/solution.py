class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        length = len(dominoes)
        result = [i for i in dominoes]
        prevPos = -1
        currPos = -1

        for i in range(length):
            if dominoes[i] == 'R' or dominoes[i] == 'L':
                prevPos = currPos
                currPos = i

                if prevPos == -1 and dominoes[currPos] == 'L':
                    for j in range(currPos+1):
                        result[j] = 'L'
                
                elif (currPos-prevPos) > 1 and prevPos >= 0 and dominoes[prevPos] == 'R' and dominoes[currPos] == 'L':
                    for j in range(prevPos, prevPos+(currPos+1-prevPos)//2):
                        result[j] = 'R'
                    for j in range(currPos+1-(currPos+1-prevPos)//2, currPos+1):
                        result[j] = 'L'
                
                elif (currPos-prevPos) > 1 and prevPos >= 0 and dominoes[prevPos] == 'R' and dominoes[currPos] == 'R':
                    for j in range(prevPos, currPos+1):
                        result[j] = 'R'
                
                elif (currPos-prevPos) > 1 and prevPos >= 0 and dominoes[prevPos] == 'L' and dominoes[currPos] == 'L':
                    for j in range(prevPos, currPos+1):
                        result[j] = 'L'
        
        if dominoes[currPos] == 'R':
            for j in range(currPos, length):
                result[j] = 'R'
        
        return ''.join(result)

