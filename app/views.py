from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from app.models import JobPost

# Create your views here.

job_titles = [
    'first job',
    'second job',
    'third job'
]

job_details = [
    'first job desc',
    'second job desc',
    'third job desc'
]

class Temp:
    x = 'temp class'

def hello(req):
    template = loader.get_template('app/hello.html')
    temp = Temp()
    list = ['a', 'b', 'c']
    
    is_authenticated = False
    
    context = { 'name':'django', 'list': list, 'temp': temp,
               'is_authenticated': is_authenticated }
    return HttpResponse(template.render(context, req))

def job_list(req):
    jobs = JobPost.objects.all()
    context = { 'jobs': jobs }
    return render(req, 'app/index.html', context)

def job(req, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        
        job = JobPost.objects.get(id=id)
        context = { 'job': job }
        template = loader.get_template('app/job_details.html')
        
        return HttpResponse(template.render(context, req))
    except:
        return HttpResponseNotFound(f'<h1>Job {id} Not Found</h1>')
    