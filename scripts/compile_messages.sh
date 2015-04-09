echo 'Compiling messages for django-i18next...'
cd src/i18next/
django-admin.py compilemessages -l de
django-admin.py compilemessages -l nl
django-admin.py compilemessages -l ru

echo 'Compiling messages for example projects...'
cd ../../examples/simple/
django-admin.py compilemessages -l de
django-admin.py compilemessages -l nl
django-admin.py compilemessages -l ru