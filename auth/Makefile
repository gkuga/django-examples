MANAGE_CMD=pipenv run python manage.py

main:
	$(MANAGE_CMD) shell < scripts/main.py

run:
	$(MANAGE_CMD) runserver

migrate:
	$(MANAGE_CMD) migrate

makemigrations:
	$(MANAGE_CMD) makemigrations

shell:
	$(MANAGE_CMD) shell

erd:
	$(MANAGE_CMD) graph_models -a -g -o erd.png
