from re import template
from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import addDoctor
from .models import DoctorList

# Create your views here.

class doctorView(View):
    form_class = addDoctor
    template_name = 'postDoctor.html'

    def get(self, req):
        form = self.form_class()
        return render(req, self.template_name, {'form':form})
    
    def post(self, req):
        form = self.form_class(req.POST)
        if form.is_valid():
            name = req.POST['name']
            age = req.POST['age']
            print(name)
            print(age)
            obj = DoctorList(name=name, age=age)
            obj.save()
            return HttpResponse('Alhamdulillah')
        return render(req, self.template_name, {'form': form})
