from django.test import TestCase
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
