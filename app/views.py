from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from app.models import User, Message
from django.shortcuts import render
from django.template import RequestContext, loader
from app.forms import ContactForm
import datetime


def detail(request, user_id):
    return HttpResponse("You're looking at poll %s." % user_id)


def results(request, user_id):
    return HttpResponse("You're looking at the results of poll %s." % user_id)


def vote(request, user_id):
    return HttpResponse("You're voting on poll %s." % user_id)


def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', {"now": now})

# t = loader.get_template('myapp/template.html')
#     c = RequestContext(request, {'foo': 'bar'})
#     return HttpResponse(t.render(c),
#         content_type="application/xhtml+xml")


def contactus(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            # subject = form.cleaned_data['subject']
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contactus.html', {
        'form': form,
    })