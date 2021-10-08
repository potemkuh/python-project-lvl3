install:
	poetry install

build:
	poetry build

package-install:
	python -m pip install dist/*.whl

loader:
	poetry run page_loader

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml