import django_filters
from . import models


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = models.Product
        fields = ['price', 'release_date']
