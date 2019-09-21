class Solution {
    int last;
    public int[] plusOne(int[] digits) {
        last = digits.length - 1;
        int[] temp = rec_plus(digits);
        if (temp[0] == 0) {
            int[] newdigits = new int[digits.length + 1];
            newdigits[0] = 1;
            temp = newdigits;
        }
        return temp;
    }
    
    public int[] rec_plus(int[] indigits){
        if (indigits[last] != 9){
            indigits[last] = indigits[last] + 1; 
        } else{
            if (last != 0){
                indigits[last] = 0;
                last --;
                rec_plus(indigits);
            } else {
                indigits[0] = 0;
            }
        }
        return indigits;
    }
}
