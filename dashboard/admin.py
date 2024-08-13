from django.contrib import admin
from .models import Student,Time_table

class StAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'allow_status')
    list_editable = ('allow_status',)

class TtAdmin(admin.ModelAdmin):
    list_display = ('student', 'entry_time', 'exit_time')

    

admin.site.register(Student,StAdmin)
admin.site.register(Time_table,TtAdmin)

