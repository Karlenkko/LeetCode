class Solution:
    def countAndSay(self, n: int) -> str:
        prev = '1'
        for i in range(1,n):
            curr = ''
            num = prev[0]
            count = 1
            for j in range(1, len(prev)):
                if prev[j] == num :
                    count += 1
                else:
                    curr += str(count) + num
                    num = prev[j]
                    count = 1
            curr += str(count) + num
            prev = curr
        return prev
