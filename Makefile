setup:
	pipenv install
	pipenv install -d
	rm -rf requirements.txt
	pipenv lock -r >> requirements.txt
typecheck: setup
	mypy --ignore-missing-imports --follow-imports=skip .
format: setup
	pyformat -i -r .
	isort -rc .
test: setup typecheck
	nosetests
build: setup
	python setup.py sdist
install: setup
	python setup.py install

