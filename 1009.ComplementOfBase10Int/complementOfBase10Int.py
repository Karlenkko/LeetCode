import math
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if (N==0): return 1
        if(N==1): return 0
        i = ~N
        i=i+math.pow(2,math.ceil(math.log(N,2)+1e-10))
        return int(i)
