from django.conf.urls import patterns, include, url

from django.contrib import admin
import contacts.views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',contacts.views.ContactsListView.as_view(),name= 'contacts-list',),
    url(r'^new$',contacts.views.CreateContactView.as_view(),name= 'contacts-new',),
    url(r'^edit/(?P<pk>\d+)$',contacts.views.UpdateContactView.as_view(),name= 'contacts-edit',),

    url(r'^contact/(?P<pk>\d+)$',contacts.views.ContactView.as_view(),name= 'contacts-view',),

    
)
