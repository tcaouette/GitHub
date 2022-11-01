
from django.urls import path
from . import views
#app_name='cdm_home'
urlpatterns = [

	path('', views.index, name='index'),
	path('contacts/', views.contacts, name='contacts')
]
