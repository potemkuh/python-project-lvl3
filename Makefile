install:
	poetry install

build:
	poetry build

package-install:
	python -m pip install dist/*.whl

loader:
	poetry run page_loader

make lint:
	poetry run flake8
