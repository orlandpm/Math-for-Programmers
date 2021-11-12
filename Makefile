default:
	cat ./Makefile
verify: 
	pycodestyle
check:
	flake8
build: 
	docker build -t jsifantu/jupyter-lab .
run: build
	docker run -p 8888:8888 -v /Users/jean-dominiquesifantus/Development/Math-for-Programmers:/home/ubuntu jsifantu/jupyter-lab
