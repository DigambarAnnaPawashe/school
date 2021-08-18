from django.contrib import admin
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    @admin.display(description='Birth decade')
    def decade_born_in(self):
        return '%d’s' % (self.birthday.year // 10 * 10)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'decade_born_in')