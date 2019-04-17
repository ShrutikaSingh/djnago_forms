from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def contact(request):
    form=ContactForm()
    #return HttpResponse('contact view') it was earlier when we dont have template
    return render(request, 'form.html', {'forms':form})
