from django import forms
from .models import Note

class noteform(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title','text','color']
        labels = {'title':'Enter Title','text':'Despcription','color':'Colour'}
        widgets={
            'title':forms.TextInput(attrs={'class':'title'}),
            # 'text':forms.Textarea(attrs={'class':'title'}),
            # 'color':forms.Select(attrs={'class':'title'}),
            # 'date':forms.DateInput(attrs={'type':'date','class':'title'})

             }