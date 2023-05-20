class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # if k > len(s):
        #     return 0
        
        # left, right=0,0
        # lst = []
        # s_set=set()
        # while right<len(s):
        #     if s[right] not in s_set:
        #         s_set.add(s[right])
                
        #     else:
        #         while s[right] in s_set:
        #             s_set.remove(s[left])
        #             left+=1
        #         s_set.add(s[right])

        #     if len(s_set)==k:
        #         lst.append(s[left:right+1])
        #         s_set.remove(s[left])
        #         left+=1
        #     right+=1
            
        # print(lst)
        # return len(lst)


        ##Follow Up question, can you optimize space?
        ## Answer: Yes, by using array of length 26 characters and increasing the counter of each character

        if k > len(s):
            return 0
        left, right=0,0
        output=0
        array = [0]*26
        while right < len(s):
            array[ord(s[right])-ord('a')]+=1
            while array[ord(s[right])-ord('a')]>1:
                array[ord(s[left])-ord('a')]-=1
                left+=1
            if right-left+1==k:
                output+=1
                array[ord(s[left])-ord('a')]-=1
                left+=1
            right+=1
        return output
