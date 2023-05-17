class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # vocab = set()
        # if len(s)==0:
        #     return 0
        # l,r=0,1
        # counter=0
        # vocab.add(s[l])
        # while r < len(s):
        #     curr = s[r]
        #     if s[r] in vocab:
        #         while s[r] in vocab:
        #             counter=max(counter, len(vocab))
        #             vocab.remove(s[l])
        #             l+=1
        #     vocab.add(s[r])
        #     r+=1
        # counter=max(counter,len(vocab))
        # return counter

        #sliding window

        i,j,ans,del_idx,dic=0,0,0,0,{}
        # if s=="" :
        #     return 0
        if len(s)<2:
            return len(s)
        while j<len(s):
            if s[j] in dic and dic[s[j]]>=i:
                i=dic[s[j]]+1
                # Instead of this, check if del_idx > i
                #If yes, then update i else, i is already ahead of deleting index, ignore it!
                # while i<=del_idx:
                #     if s[i] in dic:
                #         del dic[s[i]]
                #     i+=1
            dic[s[j]]=j
            ans=max(ans,j-i+1)
            j+=1
            
        return ans
