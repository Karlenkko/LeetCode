class CountingBits {
    public int[] countBits(int num) {
		int exp = 0;
		int length = num + 1;
		while (Math.pow(2.0, exp) <= num){
			exp++;
		}
		if (exp > 0) {
			exp--;
		}
		int maxExp = (int) Math.pow(2, exp);
		int[] binOnes = new int[length];
		int index;
		for (int i = 0; i < exp; i++){
			index = (int) Math.pow(2, i);
			for (int j =0; j < index; j++){
				binOnes[index+j] = binOnes[j] + 1;
			}
		}
		for (int i = maxExp; i < length; i++) {
				binOnes[i] = binOnes[i-maxExp] + 1;
		}
		return binOnes;
    }
}

