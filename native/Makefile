TARGETS = entropy markov

all: $(TARGETS)

clean:
	rm $(TARGETS) *.o 2> /dev/null || true

%.o: %.c
	gcc -c -o $@ $^

entropy: entropy.o
	gcc -O2 -o $@ $^ -lm

markov: markov.o
	gcc -O2 -o $@ $^

.PHONY: all clean
