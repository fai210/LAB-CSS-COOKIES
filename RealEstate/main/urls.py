from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.main_page, name='main_page'),
    path("main/properties/",views.properties_page,name='properties_page'),
     path("main/contact/",views.contact_page,name='contact_page')
]