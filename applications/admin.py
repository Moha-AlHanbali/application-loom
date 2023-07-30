from django.contrib import admin
from .models import CareerBoard, Interaction, Application


class CareerBoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'application_date', 'company_name', 'job_title', 'application_status', 'job_country']


class JobInteractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'interaction_date', 'interaction_highlight', 'interaction_description', 'associated_application']
    
    def associated_application(self, obj):
        try:
            application = obj.application_set.first()
            if application:
                return f"{application.application_date} - {application.company_name} - {application.job_title}"
            else:
                return None
        except Application.DoesNotExist:
            return None


admin.site.register(CareerBoard, CareerBoardAdmin)
admin.site.register(Application, JobApplicationAdmin)
admin.site.register(Interaction, JobInteractionAdmin)
