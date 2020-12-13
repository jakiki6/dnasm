#!/bin/bash

mkdir tmp
touch tmp/test.asm
touch tmp/test.rna
touch tmp/ref.rna

function assemble() {
	python3 ../dnasm.py -i tmp/test.asm -o tmp/test.rna > /dev/null && \
	cmp --silent tmp/test.rna tmp/ref.rna && \
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

echo -n Test 6: Sars-CoV-2 ...\ 
cat ../virus/sarscov2.asm > tmp/test.asm
python3 ../dnasm.py -i tmp/test.asm -o tmp/ref.rna > /dev/null
assemble

rm -fr tmp
