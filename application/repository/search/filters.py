import django_filters
from dal import autocomplete
from search.models import TUpSearch


class TUpSearchFilter(django_filters.FilterSet):
	
	class Meta:
		model = TUpSearch
	#	fields = ['samtypedesc']
		fields ={
		'aqid':['icontains'],
		'riskcategory':['icontains'],
		'samtypedesc':['icontains'],
		'volume':['gt','lt'],
		'gender':['icontains'],
		'age':['gt','lt'],
		}
		
	def __init__(self,*args,**kwargs):
		super(TUpSearchFilter,self).__init__(*args,**kwargs)
		if self.data =={}:
			self.queryset = self.queryset.none()
		
