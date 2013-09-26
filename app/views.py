from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from app.models import User1
from django.shortcuts import render
from app.forms import ContactForm

def index(request):
    mainuser = User1.objects.get(pk=1)
    return render(request, 'index.html', {
        'mainuser': mainuser,
    })


def edit(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            # subject = form.cleaned_data['subject']
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'edit.html', {
        'form': form,
    })