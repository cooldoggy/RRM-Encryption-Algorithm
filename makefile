.DEFAULT_GOAL := run
say_hello:
	@echo "Hello World"
run:
	clear
	python main.py
encrypttest:
	clear
	python encrypt.py
decrypttest:
	clear
	python decrypt.py
clean:
	rm -f main
	@echo Cleaned all compiled programs
