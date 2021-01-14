#!/bin/bash

passed=0
ran=0

mkdir tmp
touch tmp/test.asm
touch tmp/test.rna
touch tmp/ref.rna

function assemble() {
	ran=$((ran + 1))
	python3 ../dnasm.py tmp/test.asm -o tmp/test.rna &> /dev/null && \
	cmp --silent tmp/test.rna tmp/ref.rna && \
	passed=$((passed + 1)) && \
	echo Passed || (
		echo Failed
		echo Expected $(cat tmp/ref.rna) and got $(cat tmp/test.rna)
	)
}

echo -n Test 1: Assemble empty file ...\ 
assemble

echo -n Test 2: Simple bases ...\ 
echo bases taaaaa > tmp/test.asm
echo -n taaaaa > tmp/ref.rna
assemble

echo -n Test 3: Times opcode ...\ 
echo times 2 bases taa > tmp/test.asm
echo -n taataa > tmp/ref.rna
assemble

echo -n Test 4: start and end opcodes ...\ 
echo start > tmp/test.asm
echo nop >> tmp/test.asm
echo end >> tmp/test.asm
echo -n atgtaa > tmp/ref.rna
assemble

echo -n Test 5: acids opcode ...\ 
echo acids Start, Ala, End > tmp/test.asm
echo -n atggcttaa > tmp/ref.rna
assemble

echo -n Test 6: tail opcode ...\ 
echo start > tmp/test.asm
echo end >> tmp/test.asm
echo tail 9 >> tmp/test.asm
echo -n atgtaaaaaaaaaaa > tmp/ref.rna
assemble

echo -n Test 7: Sars-CoV-2 ...\ 
cat ../../shared/virus/sarscov2.asm > tmp/test.asm &> /dev/null
python3 ../dnasm.py tmp/test.asm -o tmp/ref.rna > /dev/null
assemble

echo -n Test 8: Protein loading system ...\ 
echo protein_db WP_001149592.1 > tmp/test.asm # I don't have that protein :(
echo -n > tmp/ref.rna
ran=$((ran + 1))
python3 ../dnasm.py tmp/test.asm -o tmp/test.rna > /dev/null && \
	cmp --silent tmp/test.rna tmp/ref.rna && \
	echo Failed || \
	echo Passed && \
	passed=$((passed + 1))

echo -n Test 9: Including test ...\ 
echo start > tmp/test.asm
echo %include tmp/test2.asm >> tmp/test.asm
echo end > tmp/test2.asm
echo -n atgtaa > tmp/ref.rna
assemble

echo Test 10: snippet database
echo -n "  1. from local database ... "
echo snippet 001cee75e7265a50f646b1bbf527ef652b0bbdc1a65d55463647e7adf8ba708a9f > tmp/test.asm
python3 ../dnasm.py ../../shared/virus/sarscov2.asm -o tmp/ref.rna &> /dev/null
assemble

rm -fr tmp

echo Summary: $passed/$ran test were successful
