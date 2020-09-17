all: feast

feast:
	gcc -m32 -fno-stack-protector -fno-pie -no-pie feast.c -o feast
	strip feast

clean:
	rm feast