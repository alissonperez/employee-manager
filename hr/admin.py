from django.contrib import admin
from hr import models

class DepartmentAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
