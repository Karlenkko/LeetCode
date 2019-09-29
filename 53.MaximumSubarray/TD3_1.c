#include <stdio.h>

int main()
{
	int n;
	int i;
	int j;
	int maxsum = 0;
	int sum = 0;
	int temp;
	scanf("%d", &n);
	int inputs[n];
	for (i = 0; i < n; i ++) {
		scanf("%d", &inputs[i]);
		if (sum <= 0) {
			sum = inputs[i];
		} else {
			sum += inputs[i];
		}
		if (maxsum < sum) {
			maxsum = sum;
		}
	}
	printf("%d\r\n", maxsum);
	return 0;
}
