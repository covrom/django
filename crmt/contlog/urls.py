from django.conf.urls import url, include
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
    
from .views import HomePageView, EditContactView, ContactsView, contact_create

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^contacts/$', ContactsView.as_view(), name='contact_list'),
    url(r'^table/', include('table.urls')),
    url(r'^edit_contact/(?P<pk>\d+)/$', EditContactView.as_view(), name='edit_contact'),
    url(r'^create_contact/$', contact_create, name='create_contact'),
]