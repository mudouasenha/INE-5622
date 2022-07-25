all:
	@echo " -\n -\n -\n O codigo está na pasta target criada aqui: \n 	./src/lexer.py \n Para executar basta rodar:\n		python src/lexer.py \n"
target:
	recipes
run:
	python lexer.py
setup: requirements.txt
	pip install -r requirements.txt
clean :
	rm -rf __pychache__