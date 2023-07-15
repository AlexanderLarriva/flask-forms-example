start:
# poetry run flask --app flask_training.example run --port 8000

# poetry run flask --app flask_training.example:app run --port 8000

	poetry run flask --app flask_training.myapp:app run

start-debug:
	poetry run flask --app flask_forms.myapp --debug run --port 8000

test:
	poetry run flake8 .
	poetry run pytest
