class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int l[][] = new int [obstacleGrid.length + 1][obstacleGrid[0].length + 1];
        l[1][0] = 1;
        for (int i = 1; i < l.length; i ++) {
            for (int j = 1; j < l[0].length; j ++) {
                if (obstacleGrid[i - 1][j - 1] == 0) {
                    l[i][j] = l[i - 1][j] + l[i][j - 1];
                }
            }
        }
        return l[obstacleGrid.length][obstacleGrid[0].length];
    }
}
