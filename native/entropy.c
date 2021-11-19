#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <limits.h>

#define BLOCK_SIZE (1 << 20)

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
	if (argc < 4) {
		return 1;
	}

	FILE *fptr = fopen(argv[1], "rb");
	long start = strtol(argv[2], NULL, 10);
	long end = strtol(argv[3], NULL, 10);

	if (end == 0) {
		end = LONG_MAX;
	}

	long to_read = end - start;

	fseek(fptr, start, SEEK_SET);

	while (1) {
		int read = fread(&block, 1, sizeof(block), fptr);
		length = length + read;

		if (read == 0 || to_read == 0) {
			break;
		}

		for (int i = 0; i < BLOCK_SIZE && to_read > 0; i++) {
			seen[block[i]]++;
			to_read--;
		}

		memset(&block, 0, sizeof(block));
	}

	check('a');
	check('t');
	check('c');
	check('g');
	entropy = entropy / 2.0f;

	printf("%f\n", entropy);

	return 0;
}
