from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)#this will populate our form with the data submitted by user
        if form.is_valid():
            name=form.cleaned_data['name']
            name=form.cleaned_data['email']
            
    form=ContactForm()
    #return HttpResponse('contact view') it was earlier when we dont have template
    return render(request, 'form.html', {'forms_11':form})
