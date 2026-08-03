run:
	python3 run.py

freeze:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt

test:
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete