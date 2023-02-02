POETRY = poetry run
.PHONY: install shell run format test sec docs


install:
	@poetry install
shell:
	@poetry shell
run:
	strawberry server src.app
format:
	@${POETRY} isort .
	@${POETRY} blue .
test:
	@${POETRY} pytest
cover:
	@${POETRY} pytest --cov=.
sec:
	@${POETRY} pip-audit
docs:
	@${POETRY} mkdocs serve
