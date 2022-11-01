import django_tables2 as tables
from search.models import TUpSearch

class TUpSearchTable(tables.Table):
	class Meta:
		model= TUpSearch
		fields =[
		'aqid',
		'gender',
		'samtypedesc',
		]	
