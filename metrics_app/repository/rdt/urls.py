
from django.urls import path
from . import views
app_name='rdt'

urlpatterns = [

	path('rdt_home', views.index, name='index_rdt'),
#	path('stg1_ecrf/', views.stg1_ecrf, name='stg1_ecrf'),
#	path('stg1_brpcr/', views.stg1_brpcr, name='stg1_brpcr'),
#	path('stg0_flu1/', views.stg0_flu1_create.as_view(), name='stg0_flu1'),
#	path('stg0_flu2/', views.stg0_flu2_create.as_view(), name='stg0_flu2'),

]
