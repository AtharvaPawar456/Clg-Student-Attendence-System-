from django.contrib import admin

from .models import TeacherData, Studentprofile, Studattendence, TimeTable

# # Register your models here.

admin.site.register(TeacherData)
admin.site.register(Studentprofile)
admin.site.register(Studattendence)
admin.site.register(TimeTable)
# admin.site.register(Employaccdata)
# admin.site.register(Msgdata)
# admin.site.register(Clusterdata)