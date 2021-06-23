.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest -vvv

.PHONY: build
build:
	poetry build

.PHONY: publish
publish: build
	poetry publish

.PHONY: test-publish
test-publish: build
	poetry publish -r instance-builder
