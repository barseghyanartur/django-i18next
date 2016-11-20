reset
./scripts/uninstall.sh
./scripts/install_django_1_7.sh
#python examples/simple/manage.py test i18next --settings=settings_django_1_7 --traceback -v 3
./runtests.py
