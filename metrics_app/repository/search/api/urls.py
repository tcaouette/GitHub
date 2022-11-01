from django.urls import path
from . import views
from search.api.views import TUPBrudView, TUPBapiView, TUPArudView, TUPAapiView

urlpatterns=[
	path('freezers/', TUPBapiView.as_view(), name='freezer-listcreate'),
	path('freezers/freezer/boxid/<str:boxid>', views.TUPBrudView.as_view(), name='freezer-rud'),
	path('aliquots/', TUPAapiView.as_view(), name='aliquot-listcreate'),
	path('aliquots/aliquot/aqid/<str:aqid>', views.TUPArudView.as_view(), name='aliquot-rud'),


]
