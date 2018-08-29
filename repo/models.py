from django.db import models
from django.contrib import admin


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Record(models.Model):
    name = models.CharField(max_length=200)
    fields = models.ManyToManyField(Field, through='RecordFields')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class RecordFields(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.TextField()


# ADMIN
class RecordFieldsInline(admin.TabularInline):
    model = RecordFields
    extra = 1


class RecordAdmin(admin.ModelAdmin):
    inlines = (RecordFieldsInline,)


class FieldAdmin(admin.ModelAdmin):
    inlines = (RecordFieldsInline,)
