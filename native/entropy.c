#include <stdio.h>
#include <math.h>
#include <string.h>

#define BLOCK_SIZE 65536

double entropy = 0.0f;
long length = 0;
int seen[256] = { 0 };
char block[BLOCK_SIZE] = { 0 };

void check(char letter) {
	double p_x = ((double) seen[letter]) / length;

	if (p_x > 0) {
		entropy = entropy - p_x * log2(p_x);
	}
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return 1;
	}

	FILE *fptr = fopen(argv[1], "rb");
	if (fptr == NULL) {
		return 1;
	}

	while (1) {
		int read = fread(&block, 1, sizeof(block), fptr);
		length = ftell(fptr);

		if (read == 0) {
			break;
		}

		for (int i = 0; i < BLOCK_SIZE; i++) {
			seen[block[i]]++;
		}

		memset(&block, 0, sizeof(block));
	}

	check('a');
	check('t');
	check('c');
	check('g');
	entropy = entropy / 2.0f;

	printf("%f\n", entropy);

	fclose(fptr);

	return 0;
}
