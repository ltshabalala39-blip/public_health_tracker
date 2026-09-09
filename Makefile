# Public health tracker Automation
.PHONY: install extract clean test

install:
		pip install -r requirements.txt

extract:
		python3 src/extract.py

clean :
		find . -type d -name "__pycache__" -exec rm -rf {} +

test  :
		pytest tests/ -v
