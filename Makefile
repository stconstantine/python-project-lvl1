# Makefile
install: # update deps
	poetry install

brain-games: # run brain_games
	poetry run brain-games

brain-even: # run brain_games
	poetry run brain-even

brain-calc: # run brain_games
	poetry run brain-calc

brain-gcd: # run brain_games
	poetry run brain-gcd

brain-progression: # run brain_games
	poetry run brain-progression

brain-prime: # run brain_games
	poetry run brain-prime

build: # build dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

build_and_install:
	make build
	make package-install