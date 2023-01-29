.PHONY: install format test

install:
	@poetry install
format:
	@poetry run isort .
	@poetry run blue .
test:
	@poetry run pytest --cov=.