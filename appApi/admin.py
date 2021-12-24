from django.contrib import admin
from .models import ProjectStagesMapping,ProjectAssigningDetails, ProjectDailyupdates
# Register your models here.


admin.site.register(ProjectStagesMapping)
admin.site.register(ProjectAssigningDetails)
admin.site.register(ProjectDailyupdates)