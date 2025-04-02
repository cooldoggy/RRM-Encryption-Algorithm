.DEFAULT_GOAL := generate
say_hello:
	@echo "Hello World"
run:
	make clean
	make generate
	clear
	./main
generate:
	make clean
	gcc main.c -o main -lm -lcrypto
debug:
	make clean
	gcc main.c -o main -g -lm -lcrypto
	gdb main
clean:
	rm -f main
	@echo Cleaned all compiled programs
