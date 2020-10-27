init:
	pip install -r requirements.txt

test:
	python -m unittest -v tests/tictactoe_helpers_test.py
