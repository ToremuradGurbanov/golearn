from django.contrib import admin

from .models import Project, Blog, Course

admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Course)