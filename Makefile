# Makefile
install: # update deps
	poetry install

brain-games: # run
	poetry run brain-games

build: # build dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl