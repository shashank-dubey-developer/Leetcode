class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1)!=len(sentence2):
            return False
        
        else:
            pairSet=set()
            for pair in similarPairs:
                pairSet.add((pair[0],pair[1]))
            for i in range(len(sentence1)):
                if sentence1[i]==sentence2[i]:
                    continue
                if not((sentence1[i],sentence2[i]) in pairSet or (sentence2[i],sentence1[i]) in pairSet):
                    return False

            return True
