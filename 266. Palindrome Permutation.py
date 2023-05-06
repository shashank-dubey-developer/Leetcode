class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count=Counter(s)
        lst = [value&1 for key,value in count.items() if value&1]
        if len(lst)>1:
            return False
        else:
            return True
