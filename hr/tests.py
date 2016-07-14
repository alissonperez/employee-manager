from unittest import mock

from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth import models as auth_models
from django.test import Client
from django.core.urlresolvers import reverse

from hr import models, factories


class DepartmentFactoryTest(TestCase):

    def test_creation_returns_department_instance(self):
        dep = factories.DepartmentFactory()
        self.assertIsInstance(dep, models.Department)


class EmployeeFactoryTest(TestCase):

    def test_creation_returns_employee_instance(self):
        emp = factories.EmployeeFactory()
        self.assertIsInstance(emp, models.Employee)

    def test_creation_must_have_department_associated(self):
        emp = factories.EmployeeFactory()
        self.assertIsInstance(emp.department, models.Department)


class PopulateCommandTest(TestCase):

    def test_call_command_must_add_admin_user(self):
        self.assertEqual(
            auth_models.User.objects.filter(username='admin').count(), 0)

        self._run_command()

        self.assertEqual(
            auth_models.User.objects.filter(username='admin').count(), 1)

    def test_call_command_must_create_departments(self):
        self.assertEqual(models.Department.objects.all().count(), 0)

        self._run_command()

        self.assertGreater(models.Department.objects.all().count(), 0)

    def test_call_command_must_create_employees(self):
        self.assertEqual(models.Employee.objects.all().count(), 0)

        self._run_command()

        self.assertGreater(models.Employee.objects.all().count(), 0)

    def _run_command(self):
        with mock.patch('hr.management.commands.populate.Command._out_success'):
            call_command('populate')


class EmployeesViewTest(TestCase):

    def setUp(self):
        # Creating some employees
        self.employees = []

        for _ in range(3):
            self.employees.append(factories.EmployeeFactory())

    def test_get_on_employees_list_returns_200(self):
        c = Client()
        response = c.get(reverse('employees'))
        self.assertEqual(response.status_code, 200)

    def test_get_on_employees_list_returns_empty_list(self):
        models.Employee.objects.all().delete()

        c = Client()
        response = c.get(reverse('employees'))
        self.assertEqual(response.json(), [])

    def test_get_on_employees_list_returns_list_of_employees(self):
        expected_result = []
        for emp in self.employees:
            expected_result.append(dict(
                name=emp.name,
                email=emp.email,
                department=emp.department.name
            ))

        c = Client()
        response = c.get(reverse('employees'))

        self.assertEqual(len(response.json()), len(self.employees))
        self.assertEqual(response.json(), expected_result)
