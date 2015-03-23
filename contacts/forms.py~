from django import forms
from django.core.exceptions import ValidationError
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    confirm_email=forms.EmailField(225, required = True)

    class Meta:
	model = Contact

    def __init__(self,*args,**kwargs):
	if kwargs.get('instance'):
	    email=kwargs['instance'].email
	    kwargs.setdefault('initial',{})['confirm_email']=email
        return super(ContactForm,self).__init__(*args,**kwargs)


    def clean(self):
	if(self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
            raise ValidationError("Emails addresses must match for both fields")
        return self.cleaned_data
