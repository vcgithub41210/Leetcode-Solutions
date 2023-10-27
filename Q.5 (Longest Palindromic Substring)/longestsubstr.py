class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        longsubstr = ''
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                templength = j-i+1
                if templength >= maxLength:
                    tempstr = s[i:j+1]
                    reverstr = tempstr[::-1]
                    if tempstr == reverstr:
                        longsubstr = tempstr
                        maxLength = templength
        return longsubstr