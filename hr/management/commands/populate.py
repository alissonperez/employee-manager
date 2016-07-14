from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from hr import factories


class Command(BaseCommand):
    help = 'Create admin user and add some fake data.'

    def handle(self, *args, **options):
        self._create_admin_user()
        self._populate()

    def _populate(self):
        self._out_success('Creating some departments.')

        departments = [
            'Architecture',
            'E-commerce',
            'Mobile',
        ]

        employees = []
        for dep_name in departments:
            department = factories.DepartmentFactory(name=dep_name)

            self._out_success('Department "{}" created! Creating some employees:'.format(department))

            for i in range(2):
                employee = factories.EmployeeFactory(department=department)
                employees.append(employee)

                self._out_success('Employee "{}" created on departement "{}"'.format(
                    employee, department))

    def _create_admin_user(self):
        if User.objects.filter(username='admin').count() > 0:
            self._out_warning('User "admin" already created.')
            return

        User.objects.create_superuser(
            'admin', 'admin@luizalabs.com', 'admin')
        self._out_success('Admin user created.')

    def _out_warning(self, message):
        self.stdout.write(self.style.WARNING(message))

    def _out_success(self, message):
        self.stdout.write(self.style.SUCCESS(message))
