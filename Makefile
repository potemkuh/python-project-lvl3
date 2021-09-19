install:
	poetry install

build:
	poetry build

package-install:
	python -m pip install dist/*.whl

loader:
	poetry run loader
