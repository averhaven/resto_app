setup:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

test:
	PYTHONPATH=. venv/bin/pytest

run:
	sh run_flask.sh

clean:
	rm -r venv