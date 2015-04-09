reset
./scripts/uninstall.sh
./scripts/install_django_1_5.sh
python examples/simple/manage.py test i18next --traceback -v 3