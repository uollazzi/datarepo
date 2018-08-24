from django.contrib import admin

# Register your models here.
from .models import Field, Record, RecordFields, RecordAdmin, FieldAdmin

admin.site.register(Record, RecordAdmin)

admin.site.register(Field, FieldAdmin)
