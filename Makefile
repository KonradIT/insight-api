.DEFAULT: install
install:
	python setup.py install
make: 
	python setup.py sdist
deploy:
	sudo python setup.py sdist bdist_wheel
	twine upload dist/*
