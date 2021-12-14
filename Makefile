start_db:
	flask db init
	flask db migrate
	flask db upgrate

start_translations:
	pybabel extract -F babel.cfg -k _l -o messages.pot .
	pybabel init -i messages.pot -d app/translations -l pt

run:
	python manage.py

rebuild_translations:
	pybabel extract -F babel.cfg -k _l -o messages.pot .
	pybabel update -i messages.pot -d app/translations

compile_translations:
	pybabel compile -d app/translations