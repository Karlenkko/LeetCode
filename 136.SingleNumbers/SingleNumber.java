class SingleNumber {
    public int singleNumber(int[] nums) {
        int a = 0;
        for (int i : nums) {
            a = a ^ i;
        }
        return a;
    }
}
