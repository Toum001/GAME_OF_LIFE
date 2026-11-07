PYTHON = python3
APP = main.py

.PHONY: help run clean

help:
	@echo "Available commands:"
	@echo "  make run       Launch the Game of Life"
	@echo "  make clean     Remove Python cache files"

run:
	$(PYTHON) $(APP)

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
