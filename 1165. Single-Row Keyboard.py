class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyDict={}
        counter,ans,prev=0,0,0
        for letter in keyboard:
            keyDict[letter]=counter
            counter+=1
        for letter in word:
            ans+=abs(keyDict[letter]-prev)
            prev=keyDict[letter]
        return ans
