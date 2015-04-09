pip install -r examples/requirements.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static
python examples/simple/manage.py collectstatic --noinput
python examples/simple/manage.py syncdb --noinput
python examples/simple/manage.py migrate --noinput
python examples/simple/manage.py i18next_create_test_data