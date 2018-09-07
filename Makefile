setup:
	pipenv install
	pipenv install -d
	rm -rf requirements.txt
	pipenv lock -r >> requirements.txt
format: setup
	pyformat -i -r .
	isort -rc .
build: setup
	python setup.py sdist
install: setup
	python setup.py install

