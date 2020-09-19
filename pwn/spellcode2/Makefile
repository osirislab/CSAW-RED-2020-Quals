all: spellcode2

spellcode2:
	gcc -z execstack -fno-pie -no-pie level_2_spellcode.c -o level_2_spellcode
	strip level_2_spellcode

clean:
	rm level_2_spellcode