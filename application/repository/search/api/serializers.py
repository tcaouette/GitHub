from rest_framework import serializers
from search.models import TUpInventoryb, TUpInventorya

class TUPBSerializer(serializers.ModelSerializer):
	class Meta:
		model = TUpInventoryb
		fields=[
		'freezer',
		'cage',
		'cane',
		'stack',
		'boxid',
		'invnum',
		'insertdate',
		'invcomments',
		]

class TUPASerializer(serializers.ModelSerializer):
	class Meta:
		model = TUpInventorya
		fields=[
		'aqid',
		'originalid',
		'labelinfo',
		'volume',
		'insertdate',
		'invnum',
		]
