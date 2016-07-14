from django.contrib import admin
from hr import models


class DepartmentAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

    list_filter = ('department',)
    search_fields = ('name',)


admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Employee, EmployeeAdmin)
