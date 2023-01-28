install:
	@poetry install
format:
	@isort .
	@blue .
test:
	@pytest -v