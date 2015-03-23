from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView

from django.core.urlresolvers import reverse

from contacts.models import Contact
from contacts import forms


# Create your views here.
class ContactsListView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class CreateContactView(CreateView):
    model=Contact
    template_name='edit_contact.html'
    form_class = forms.ContactForm
    

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self,**kwargs):
	context=super(CreateContactView,self).get_context_data(**kwargs)
	context['target']=reverse('contacts-new')
	return context 

class UpdateContactView(UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
    
    def get_success_url(self):
        return reverse('contacts-list') 

    def get_context_data(self,**kwargs):
	context=super(UpdateContactView,self).get_context_data(**kwargs)
	context['target']=reverse('contacts-edit',kwargs={'pk':self.get_object().id})
	return context 


class ContactView(DetailView):
    model = Contact
    template_name ='contact.html'
    
