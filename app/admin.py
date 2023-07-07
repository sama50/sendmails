from django.contrib import admin
from app.models import SendMailsModel
# Register your models here.

@admin.register(SendMailsModel)
class SendMailsModelAdmin(admin.ModelAdmin):
    list_display = ('id','file','is_schedule','schedule_time')
