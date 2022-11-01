from django import forms
from search.models import TUpCoa, TRefSite, TUpSearch, TUpInventoryb, TListInventoryb, TListInventorya,Tblboxinfo,TUpInventorya
#from haystack.forms import SearchForm



class BoxForm(forms.ModelForm):
	#boxid = forms.CharField(widget=forms.Textarea(attrs={'class':'input-bordered'}))
	boxid=forms.CharField(required=True,max_length=255, min_length=1, label="Box ID")
	freezer=forms.CharField(required=True,max_length=255, min_length=1, label="Freezer")
	cage=forms.CharField(required=True,max_length=255, min_length=1, label="Cage")
	cane=forms.CharField(required=True,max_length=255, min_length=1, label="Cane")
	stack=forms.CharField(required=True,max_length=255, min_length=1, label="Stack")
	class Meta:
		model = TUpInventoryb
		fields = [
		'boxid',
		'freezer',
		'cage',
		'cane',
		'stack',
	#	'invnum',
		'insertdate',
		'invcomments'
		]

class BoxContinueCreateForm(forms.ModelForm):

	boxtype=forms.CharField(required=True,max_length=255, min_length=1, label="Box Type")
	contents=forms.CharField(required=True,max_length=255, min_length=1, label="Contents")
	class Meta:
		model = Tblboxinfo
		fields = [
		'boxid',
		'boxtype',
		'contents',
		'insertdate',
		'invstatus'
		]
class BoxUpdateForm(forms.ModelForm):
	reason = forms.CharField(widget=forms.Textarea(attrs={'class':'input-bordered'}))
	class Meta:
		model = TUpInventoryb
		fields = [
		'boxid',
		'freezer',
		'cage',
		'cane',
		'stack',
	#	'invnum',
		'insertdate',
		'invcomments'
		]

class BoxContinueUpdateForm(forms.ModelForm):
#	reason = forms.CharField(widget=forms.Textarea(attrs={'class':'input-bordered'}))
	class Meta:
		model = Tblboxinfo
	#	exclude =('boxid',)
		fields = [
		'boxid',
		'boxtype',
		'contents',
		'insertdate',
		'invstatus'
		]
class LocationForm(forms.ModelForm):
	class Meta:
		model = TRefSite
		fields=[
		#'siteid',
		'sitestate',
		'sitecountry',
		'sitename',
		'siteabbr'
		]

class AliquotForm(forms.ModelForm):
	class Meta:
		model = TUpSearch
		fields=[
#		'lotid',
		'trialkey',
		'studyid',
		'studydesc',
		'aqid',
		'originalid',
		'grid',
		'labelinfo',
		'volume',
		'insertdate',
		'invnum',
		'invcomment',
		'boxid',
		'checkout',
		'date_changed',
		'user',
		'age',
		'gender',
		'demogroup',
		'riskcategory',
		'riskgroupdesc',
		'bloodtype',
		'hiv1',
		'hiv2',
		'hivo',
		'hbs',
		'hbc',
		'hav',
		'hcv',
		'mmrv',
		'influenza',
		'sars_cov2',
		'other',
		'manufacturer',
		'panelname',
		'paneldesc',
		'membernum',
		'samtypedesc',
		'samprepdesc',
		'notes',
		'dup',
		'isconfirmed',	
		
		]

class AliquotUpdateForm(forms.ModelForm):
	reason = forms.CharField(widget=forms.Textarea(attrs={'class':'input-bordered'}))
	freeze_thaw = forms.IntegerField(required=True)
	class Meta:
		model = TUpSearch
		fields=[
#		'lotid',
		'trialkey',
		'studyid',
		'studydesc',
		'aqid',
		'originalid',
		'grid',
		'labelinfo',
		'volume',
		'insertdate',
		'invnum',
		'invcomment',
		'boxid',
		'checkout',
		'date_changed',
		'user',
		'age',
		'gender',
		'demogroup',
		'riskcategory',
		'riskgroupdesc',
		'bloodtype',
		'hiv1',
		'hiv2',
		'hivo',
		'hbs',
		'hbc',
		'hav',
		'hcv',
		'mmrv',
		'influenza',
		'sars_cov2',
		'other',
		'manufacturer',
		'panelname',
		'paneldesc',
		'membernum',
		'samtypedesc',
		'samprepdesc',
		'notes',
		'dup',
		'isconfirmed',	
		'freeze_thaw',
		]
	


class BoxInfoForm(forms.ModelForm):
	class Meta:
		model = Tblboxinfo

		fields=[
		'boxid',
		'boxtype',
		'contents',
		'insertdate'
		]		







