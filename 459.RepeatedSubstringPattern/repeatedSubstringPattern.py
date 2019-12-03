class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size=len(s)
        for i in range(0,int(size/2)):
            temp=int(size/(i+1))
            if(temp*(i+1)==size):
                if(s[0:i+1] * temp==s):
                    return True
        return False
