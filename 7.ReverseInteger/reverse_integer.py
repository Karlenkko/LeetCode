class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) >= math.pow(2,31) :
            return 0
        flag = 1
        if x > 0 : 
            flag = 0
        x = abs(x)
        result = 0;
        power = 1;
        while x >= 10 :
            temp = x % 10
            result += temp
            result *= 10
            x //= 10
        result += x
        if abs(result) >= math.pow(2,31) :
            return 0
        if flag == 0 :
            return result
        else :
            return result * (-1)               
