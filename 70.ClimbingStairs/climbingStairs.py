class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        tab = [0 for i in range(0,n)]
        tab[0] = 1
        tab[1] = 2
        for x in range(2,n):
            tab[x] = tab[x - 1] + tab[x - 2]
        return tab[n - 1]
