.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest -vvv

.PHONY: export
export:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: build
build: export
	poetry build

.PHONY: publish
publish: build
	poetry publish

.PHONY: test-publish
test-publish: build
	poetry publish -r instance-builder
