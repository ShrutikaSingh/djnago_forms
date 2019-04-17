from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,SnippetForm
# Create your views here.
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)#this will populate our form with the data submitted by user
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']

    form=ContactForm()
    #return HttpResponse('contact view') it was earlier when we dont have template
    return render(request, 'form.html', {'forms_11':form})
    #call the {{forms_11}} in the template form.html after the csrf token
    #to see the from to the route that is speciefied  for this viewin urls.py


def snippet_detail(request):
    name='dummy'
    if request.method=='POST':
        form2=SnippetForm(request.POST)#this will populate our form with the data submitted by user
        if form2.is_valid():
            form2.save()
            name=form2.cleaned_data['name']
            print(name)
    form2=SnippetForm()
    #return HttpResponse('contact view') it was earlier when we dont have template
    args={'forms_22':form2,'name':name}
    return render(request, 'snippet_form.html', args)
    #call the {{forms_22}} in the template snippet_form.html after the csrf token to see the form
    #to see the from to the route that is speciefied  for this view (i.e snippet_detail view)in urls.py
