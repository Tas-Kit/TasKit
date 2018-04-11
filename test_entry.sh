pylint --load-plugins pylint_django basic main taskit

coverage run manage.py test -v 2
coverage html