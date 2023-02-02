POETRY = poetry run
.PHONY: install shell run format test sec docs image cont


install:
	@poetry install
shell:
	@poetry shell
run:
	@${POETRY} strawberry server --port 8080 src.app
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

image:
	docker build -t passimage .
cont:
	docker run -d --name passcontainer -p 8080:8080 passimage