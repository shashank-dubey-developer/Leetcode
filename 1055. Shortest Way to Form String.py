import math
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ############# Instead of circular array, I multiplied source by length of target making it largest common subsequence ###########
        # i,j=0,0
        # s = source*len(target)
        # while j<len(target):
        #     if i==len(s):
        #         return -1
        #     elif s[i]==target[j]:
        #         j+=1
        #     i+=1
        # return (math.floor((i-1)/len(source))+1)


        ################# Here I implemented circular array ##############
        i,j,counter,answer = 0,0,0,1
        source_len,target_len=len(source),len(target)
        limit=source_len*target_len

        while j<target_len:
            if counter==limit:
                return -1
            if i==source_len:
                i=0
                answer+=1
            if source[i]==target[j] and i<source_len:
                j+=1
                i+=1
            else:
                i+=1
            
            counter+=1
        return answer
            
