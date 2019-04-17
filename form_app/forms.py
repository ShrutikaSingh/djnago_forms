from django import forms
from .models import Snippet

class ContactForm(forms.Form):  #its not bound to any model
        name=forms.CharField()
        email=forms.EmailField(label='E-mail')
        category=forms.ChoiceField(choices=[('question','Question'),('other','Other')])#array of tupples
        subject=forms.CharField(required=False)
        body=forms.CharField(widget=forms.Textarea)#widgests are used to represent actual html representation of a vield #by default widget is text input therefore we write widget here to make it large more space i.e textarea not textinput

class SnippetForm(forms.ModelForm):  #its a model form
    class Meta: #that is the fields that we want to include in our data
        model =Snippet
        fields = ('name','body',)#its a tuple
