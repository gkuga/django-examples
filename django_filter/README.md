```console
mkdir django_filter
cd django_filter
PIPENV_PYTHON=/home/gkuga/.asdf/shims/python pipenv install
pipenv install Django
pipenv shell
python -m django startproject django_filter .
python manage.py migrate
python manage.py runserver 9080
```

Create some objects and test filtering:

```console
python manage.py shell
Product.objects.create(name="foo", price=100, release_date=timezone.now(), manufacturer=Manufacturer.objects.create())
```
