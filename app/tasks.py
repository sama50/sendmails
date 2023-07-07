from celery import shared_task 
from .models import SendMailsModel 
from datetime import datetime
import pandas as pd 

from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import make_aware

@shared_task(bind=True)
def send_without_time(self,pk):  
    send_mail_helper(pk)

def send_mail_helper(pk):
    obj = SendMailsModel.objects.get(pk=pk)
    csv_file = obj.file.path
    df = pd.read_csv(csv_file) 
    for index, row in df.iterrows():
        print(row['Email'],row['Message'])
        send_email(row['Email'],row['Message'])
    obj.is_done = True
    obj.save()

@shared_task
def send_scheduled_mails():
    current_datetime = datetime.now()
    current_datetime.tzinfo
    settings.TIME_ZONE
    current_datetime = make_aware(current_datetime)
    current_datetime.tzinfo 
    all_mails = SendMailsModel.objects.filter(is_schedule=True,is_done=False).filter(schedule_time__lte=current_datetime)
    for data in all_mails:
        send_mail_helper(data.id)
   
def send_email(email,message):
    subject = 'Hello from Django' 
    from_email = 'mhaskesamadhan223@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
 