all: spellcode1

spellcode1:
	gcc -m32 -fno-stack-protector -z execstack -fno-pie -no-pie level_1_spellcode.c -o level_1_spellcode
	strip level_1_spellcode

clean:
	rm level_1_spellcode