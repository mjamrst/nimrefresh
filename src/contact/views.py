from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.

from .forms import ContactForm

def home(request):
    
    return render_to_response("home.html",
                                    locals(),
                                    context_instance=RequestContext(request))

def contactus(request):
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        subject = 'Thanks for contacting Next Impulse'
        message = 'Thanks so much for reaching out! \n We will be in touch soon before you know it.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, 'Thanks for reaching out')
        return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request))

def about(request):
    
    return render_to_response("about.html",
                                    locals(),
                                    context_instance=RequestContext(request))

def campaigns(request):
    
    return render_to_response("campaigns.html",
                                    locals(),
                                    context_instance=RequestContext(request))

def pricing(request):
    
    return render_to_response("pricing.html",
                                    locals(),
                                    context_instance=RequestContext(request))

def thanks(request):
    
    return render_to_response("thanks.html",
                                    locals(),
                                    context_instance=RequestContext(request))
