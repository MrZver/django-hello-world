test:
	PYTHONPATH=.:$(PYTHONPATH) \
	DJANGO_SETTINGS_MODULE=django_study.settings \
	django-admin.py test app