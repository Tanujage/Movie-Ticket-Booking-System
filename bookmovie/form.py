from django import forms
from .models import customer


class customform(forms.ModelForm):
    class Meta:
        model = customer
        fields=('fname','sname','mobno','photo')
        labels = {
            'fname': "Enter your First name",
            'sname': "Enter your Surname",
            'mobno': "Enter your Mobile number",
            'photo':'Upload your Photo'
        }
        widgets={
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'sname': forms.TextInput(attrs={'class': 'form-control'}),
            'mobno': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }