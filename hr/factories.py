import factory
from hr import models


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Department

    name = factory.Faker('word')


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Employee

    name = factory.Faker('name')
    email = factory.Faker('email')
    department = factory.SubFactory(DepartmentFactory)
