from django.urls import path, include
from django.conf.urls import url
from . import views
from search.views import coa,locations, big_table,SamTypeDesc, AliquotDispose,AliquotFreezeThaw,AliquotCreateMulti,BoxGrid,AliquotShipping,AliquotShippingReturn,LocationCreate

app_name='search'

urlpatterns = [

	path('', views.index, name='index'),
	path('freezer_b/', views.freezer_B, name='search_freezer_b'),
	path('freezer_a/', views.freezer_A, name='search_freezer_a'),
	path('help/', views.help_me, name='help'),

	path('freezer_contents/',views.ContentsDetailView.as_view(), name='content_detail'),
	path('aliquot/', views.aliquot, name ='aliquot'),
	path('locations/', views.locations, name ='locations'),
	path('CoA/', views.coa, name ='coa'),

	path('aliquot_add/', views.AliquotCreate.as_view(), name = 'aliquot_add'),
	path('add_location/', views.LocationCreate.as_view(), name = 'add_location'),
	path('<str:pk>/aliquot_add_multi/', views.AliquotCreateMulti.as_view(), name = 'aliquot_add_multi'),
	path('<str:pk>/aliquot_update/', views.AliquotUpdate.as_view(), name = 'aliquot_update'),

	path('aliquot_delete/<str:pk>', views.AliquotDelete.as_view(), name = 'aliquot_delete'),
	path('aliquot_table/', views.aliquot_table, name= 'aliquot_table'),
	path('meta_table/', views.meta_table, name= 'meta_table'),
	path('csv_upload/', views.csv_upload, name= 'csv_upload'),

	path('box/', views.box, name ='box'),
	

	path('aliquot_detail/<str:pk>/',views.AliquotList2, name='aliquot_detail'),
	path('aliquot_shipping/<str:pk>/',views.AliquotShipping, name='shipping'),
	path('shipping_returns/',views.AliquotShippingReturn, name='shipping_return'),
	path('boxgrid/<str:pk>/',views.BoxGrid, name='box_grid'),
	path('aliquot_dispose/<str:pk>/',views.AliquotDispose, name='aliquot_dispose'),
	path('freeze_thaw/',views.AliquotFreezeThaw, name='freeze_thaw'),
	path('freezer/',views.FreezerList, name='freezer'),



	path('box_add/', views.BoxCreate.as_view(), name = 'box_add'),
	path('box_add/continue/', views.BoxContinueCreate.as_view(), name = 'box_add_continue'),
	path('<str:pk>/box_update/', views.BoxUpdate.as_view(), name = 'box_update'),
	path('<str:pk>/box_update/continued/', views.BoxContinueUpdate.as_view(), name = 'box_continue'),

	path('box_delete/<str:pk>', views.BoxDelete.as_view(), name = 'box_delete'),
	path('login/', views.login, name ='login'),
#	#path('aliquot_search/', views.aliquot_search, 'aliquot_search'),
#	url(r'^haystack_search/', include('haystack.urls'), name='haystack_search'),
	#path('search/aliquots/', AliquotSearchView.as_view(), name ='aliquot_search'),
	path('search/aliquots/', views.search_aliquot, name ='aliquot_search'),
	path('big_table/aliquots/', big_table.as_view(), name ='big_table'),
	url('samtypedesc/$', SamTypeDesc.as_view(), name='samtypedesc'),
]
