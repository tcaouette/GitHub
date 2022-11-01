
from django.urls import path
from . import views
#from . import metrics
app_name='metrics'

urlpatterns = [

	path('rvp_metrics/', views.rvp_metrics, name='metrics'),

]
