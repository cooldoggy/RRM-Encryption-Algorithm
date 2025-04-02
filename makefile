.DEFAULT_GOAL := generate
say_hello:
	@echo "Hello World"
test:
	make clean
	make generate
	clear
	./main -r
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