from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Person(models.Model):
    class Meta:
        permissions = [("can_eat_pizzas", "Can eat pizzas")]


class Student(Person):
    class Meta:
        proxy = True
        permissions = [("can_deliver_pizzas", "Can deliver pizzas")]
