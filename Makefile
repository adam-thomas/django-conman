SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " make test | Run the tests."

test:
	@coverage run ./tests/run.py
	@coverage report --show-missing