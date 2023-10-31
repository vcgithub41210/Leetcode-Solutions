class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref

        arr = []
        for i in range(0,len(pref)):
            if i == 0: arr.append(pref[0])
            else:
                arr.append(pref[i] ^ pref[i-1])
        return arr