#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define depth 10

int state[(1 << (depth * 2))] = { 0 };
char buffer[depth];

long encode(char data[depth]) {
	long res = 0;

	for (int i = 0; i < depth; i++) {
		res = res << 2;
		switch (data[i]) {
			case 'a': res = res | 0b00; break;
			case 't': res = res | 0b01; break;
			case 'c': res = res | 0b10; break;
			case 'g': res = res | 0b11; break;
			default: res = res >> 2;
		}
	}

	return res;
}

int main(int argc, char *argv[]) {
	if (argc < 3) {
		return 1;
	}

	FILE *fptr = fopen(argv[1], "rb");
	if (fptr == NULL) {
		return 1;
	}

	while (1) {
		long ptr = ftell(fptr);

		memset(&buffer, 0, sizeof(buffer));
		int read = fread(&buffer, 1, sizeof(buffer), fptr);

		if (read == 0) {
			break;
		}

		int id = encode(buffer);
		state[id]++;
		ptr++;
		fseek(fptr, ptr, SEEK_SET);
	}

	fclose(fptr);
	fptr = fopen(argv[2], "wb");

	fwrite(&state, sizeof(state), 1, fptr);

	fclose(fptr);
}
