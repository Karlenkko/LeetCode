class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        double e = 0.1;
        double a = 1;
        double b = (a + x / a) / 2.0;
        while (a - b > e || b - a > e) {
            a = b;
            b = (a + x / a) / 2.0;
        }
        if ((int)a * (int)a > x) a = a - 1;
        return (int)a;
    }
}
