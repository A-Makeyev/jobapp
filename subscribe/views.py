from django.shortcuts import redirect, render
from django.urls import reverse
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm

# Create your views here.

def subscribe(req):
    subscribe_form = SubscribeForm()
    email_error_empty = ''
    
    if req.POST:
        subscribe_form = SubscribeForm(req.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
        
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # email = subscribe_form.cleaned_data['email']
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            
        # if email == '':
        #     email_error_empty = 'email is empty'
        
    context = { 'form': subscribe_form, 'email_error_empty': email_error_empty }
    return render(req, 'subscribe.html', context)
    
def thank_you(req):
    context = {}
    return render(req, 'thank_you.html', context)
    