wget -O django_i18next_example_app_installer.tar.gz https://github.com/barseghyanartur/django-i18next/archive/stable.tar.gz
virtualenv i18next
source i18next/bin/activate
mkdir django_i18next_example_app_installer/
tar -xvf django_i18next_example_app_installer.tar.gz -C django_i18next_example_app_installer
cd django_i18next_example_app_installer/django-i18next-stable/examples/simple/
pip install -r ../requirements/demo.txt
pip install -e git+https://github.com/barseghyanartur/django-i18next@stable#egg=django-i18next
mkdir ../media/
mkdir ../media/static/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp settings/local_settings.example settings/local_settings.py
echo "from .dev import *" > settings/__init__.py
./manage.py syncdb --noinput --traceback -v 3
./manage.py migrate --noinput
./manage.py collectstatic --noinput --traceback -v 3
./manage.py runserver 0.0.0.0:8001 --traceback -v 3
