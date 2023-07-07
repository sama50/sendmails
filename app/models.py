from django.db import models
# Create your models here.

class SendMailsModel(models.Model):
    file = models.FileField(upload_to='media')
    is_schedule = models.BooleanField(default=False)
    schedule_time  = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    is_done = models.BooleanField(default=False)