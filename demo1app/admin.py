from django.contrib import admin

from demo1app import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Student_registration)
admin.site.register(models.Parent_registration)
admin.site.register(models.Attendance)

