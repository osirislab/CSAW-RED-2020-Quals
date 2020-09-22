all: fabricator

fabricator:
	gcc -static -fno-stack-protector -fno-pie -no-pie fabricator.c -o fabricator -lcrypto
	strip fabricator

clean:
	rm fabricator