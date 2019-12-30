from django.contrib import admin
from .models import Courseregister


from .models import Courseregister2

@admin.register(Courseregister)
class CourseregisterAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'dept', 'roll')





@admin.register(Courseregister2)
class Courseregister2Admin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'dept', 'roll')