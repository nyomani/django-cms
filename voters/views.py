from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm,PassportUpload
from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonRegistration
from passporteye import read_mrz
from django.views.generic import (
    ListView,View
)
from django.db.models import Q

def home(request):
    return render(request,'voter/home.html',{'title':'Voter'})

def add(request):
    if request.method == 'POST':
        form = PersonForm(data=request.POST)
        form.save()
    form = PersonForm

    return render(request,'voter/add_person.html',{'title':'Voter-add','form':form})

def uploadPassport(request):
    print('UPLOAD')
    if request.method == 'POST':
        file_obj = request.FILES.get('file', None)
        print('file',file_obj)
        if file_obj:
            print('MRZ ',file_obj)
            mrz = read_mrz(file_obj)
            form = PersonForm()
            print(mrz)
            return render(request,'voter/add_person.html',{'title':'Voter-add','form':form})
    
    return render(request,'camera-capture.html')

class PersonSearchResulView(ListView):
    model = PersonRegistration
    template_name = 'voter/person-list.html'
    context_object_name = 'items'
    paginate_by = 6

    def get_queryset(self):
        search_crit= self.request.GET.get('search_criteria')
        nameFilter=''
        cityFilter=''
        if (search_crit):
            fields = search_crit.split(',')
            nameFilter = fields[0]
            if (len(fields)==1):
                cityFilter=''
            else:
                cityFilter = fields[1]
        registration= PersonRegistration.objects.filter(
            Q(person__first_name__contains =nameFilter)|
            Q(person__last_name__contains =nameFilter),
            Q(person__city__contains = cityFilter))
        return registration

