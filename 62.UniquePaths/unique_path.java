class Solution {
    public int uniquePaths(int m, int n) {
        int l[][] = new int [n + 1][m + 1];
        l[1][0] = 1;
        for (int i = 1; i < n + 1; i ++) {
            for (int j = 1; j < m + 1; j ++) {
                l[i][j] = l[i][j - 1] + l[i - 1][j];
            }
        }
        return l[n][m];
    }
}
