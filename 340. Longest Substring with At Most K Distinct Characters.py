class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i,j,ans,dic=0,0,0,{}
        if not k:
            return k
        while j<len(s):
            dic[s[j]]=j

            if len(dic)==k+1:
                del_idx=min(dic.values())
                del dic[s[del_idx]]
                i=del_idx+1
                
            ans=max(ans,j-i+1)
            j+=1
        return ans
                
