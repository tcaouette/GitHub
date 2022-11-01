from django.urls import path
from . import views
app_name='ihab'
urlpatterns = [

	path('ihab_home', views.index, name='index_home'),
	#path('dep_1/', views.stg1_ihab_de_1_Create.as_view(), name='data_entry1'),
	#path('dep_2/', views.stg1_ihab_de_2_Create.as_view(), name='data_entry2'),
	path('bld_primary/', views.BLD_Primary_Create.as_view(), name='bld_primary'),
	path('bld_secondary/', views.BLD_Secondary_Create.as_view(), name='bld_secondary'),
	path('bcw_primary/', views.BCW_Primary_Create.as_view(), name='bcw_primary'),
	path('bcw_secondary/', views.BCW_Secondary_Create.as_view(), name='bcw_secondary'),
	path('contacts/', views.contacts, name='contacts'),
	path('metrics/', views.metric, name='metric')
]
