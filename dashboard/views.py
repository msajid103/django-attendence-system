from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models  import Time_table, Student
import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

current = datetime.datetime.now()
today = current.strftime('%Y-%m-%d')
date_time = current.strftime('%Y-%m-%d %H:%M:%S')
# date = timezone.now()

# Print the formatted time
students = []
@csrf_exempt
def home(request): 
    if request.method == "POST":
        roll_no = request.POST.get('roll')
        password = request.POST.get('password')
        try:
            s = Student.objects.get(roll_no=roll_no, password = password)            
        except (Student.DoesNotExist):
            return render(request,'index.html',{'message':'Incorrect password or roll no'})  

        if s.allow_status:
            try:         
                s1 = Time_table.objects.get(student = s, entry_time__date = today)
                
                print('Exite status = ',s1.exit_time)
                if s1.exit_time is None:
                    s1.exit_time = date_time          
                    s1.save()            
                    return render(request,'index.html',{'message':'Succesfully Exit'})                
                return render(request,'index.html',{'message':'Already Exit'})
            except(Time_table.DoesNotExist):                   
                s1 = Time_table(student = s,entry_time = date_time)          
                s1.save()
                return render(request,'index.html',{'message': "Succesfully Enter"}) 
        else:
            return render(request,'index.html',{'message': "Your Are Not Allowed To Enter To University"})  



            # return redirect('../rector',{'message':'Error'}) 
        

    return render(request,'index.html')


    

def rector(request):
    time = datetime.datetime.now().strftime("%A %B %d %H:%M:%S")
    data = {
            'time':time,
             'students':students
            }   
  
     
    return render(request,'rector.html',data)