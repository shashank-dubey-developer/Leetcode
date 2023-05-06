class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping={}
        ans=[]
        for index,num in enumerate(nums2):
            mapping[num]=index
        for num in nums1:
            ans.append(mapping[num])
        return ans
