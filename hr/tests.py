from unittest import mock

from django.core.management import call_command
from django.test import TestCase
from django.contrib.auth import models as auth_models

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
