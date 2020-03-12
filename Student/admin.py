from django.contrib import admin

# Register your models here.
from Student.models import Stud, Certification


@admin.register(Stud)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass
