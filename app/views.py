from django.shortcuts import render , redirect
from .tasks import send_without_time
import pandas as pd
from datetime import datetime
from pytz import timezone
from .models import SendMailsModel
from django.conf import settings


def home(request):
    # add.delay()
    # send_email(request)
    if request.method == 'POST':
        file = request.FILES.get('file')
        schedule = request.POST.get('schedule')
        scheduletime = request.POST.get('scheduletime')
        
        Headers = ['Email','Message']
        print("================================")
        df = pd.read_csv(file)
        print("================================")
        uploaded_file_header_list = df.columns.tolist()
        for fields in Headers: 
            if fields not in uploaded_file_header_list:
                return redirect('/')
        data = SendMailsModel(file=file)
        data.save()
        print(file)
        print(schedule)
        print(scheduletime)
        if schedule: 
            data.is_schedule = True
            datetime_obj = datetime.strptime(scheduletime, '%Y-%m-%dT%H:%M')
            datetime_obj = timezone(settings.TIME_ZONE).localize(datetime_obj)
            
            data.schedule_time = datetime_obj
            data.save() 
             
        else:
            pass
            # send_without_time.apply_async(args=[data.id])
    return render(request,'index.html')


