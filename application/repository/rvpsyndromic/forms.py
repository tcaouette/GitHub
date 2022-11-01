import pytz
import datetime
from datetime import timedelta
from django.utils import timezone
from django import forms
from rvpsyndromic.models import TStg0Brpcr, TStg0Ecrf, TStg0Refcov2Pcr1, TStg0Refcov2Pcr2, TStg0Refflupcr1, TStg0Refflupcr2, TStg1Brpcr, TStg1Cov2Pcr, TStg1Ecrf, TStg1FlupcrUpdate,TStg1BrpcrUpdate,TStg1EcrfUpdate,TStg1Cov2Update, TStg1Cov2,TStg1ReffluMismatch,TStg1ReffluMatch
####insert names of the class models

utc=pytz.UTC

CHOICES=[
	('1','Exclude'),
	('0','Not Excluded'),
	]
DEP=[
	(1,'Data Entry Person 1'),
	(2,'Data Entry Person 2'),
	]
SITE_CHOICES=[
	('','---'),
	('cdg','CDG'),
	('euf','EUF'),
	('gen','GEN'),
	]
INTERP_CHOICES=[
	('','---'),
	('positive','Positive'),
	('negative','Negative'),
	('unknown','Unknown'),
	]
SEX_CHOICES=[
	('','---'),
	('M','Male'),
	('F','Female'),
	]	

class Stg0_flu1(forms.ModelForm):
	
	reffluexcld=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(),label="Exclude?")	
	sample=forms.CharField(required=True,max_length=6, min_length=6,label="Sample ID")
	class Meta:
		model = TStg0Refflupcr1
		exclude = ('refflupcrrow_1',)
		fields =[		
                        'refflufile_name',
			'reffluoperator',                       		
                        'refflu_date',
			'refflukitname',
			'refflukitlot',
    			'refflukitexp', 
			#'ref1_entered_by',
			#'ref1_entereddate',
			#'refflu_date', 
                        'sample', 
                        'refflua_well',
                        'refflua_cqvalue',
                        'refflua_interp',
                        'refflub_cqvalue',
                        'refflub_interp',
			'refrsv_cqvalue',
			'refrsv_interp',
                        'refnotes',
			'reffluexcld',
                        ]
 
		labels={'refflufile_name':'File Name',
			'reffluoperator':'Operator',
			'refflu_date':'Reference Date*',
			'refflukitname':'Reference Kit Name',
			'refflukitlot':'Reference Kit Lot',
			'refflukitexp':'Reference Kit Expiration',
			'sample':'Sample',
			'refflua_well':'Reference Flu A Well',
			'refflua_cqvalue':'Reference Flu A CQ Value',
			'refflua_interp':'Reference Flu A Interpretation*',
			'refflub_cqvalue':'Reference Flu B CQ Value',
			'refflub_interp':'Reference Flu B Interpretation*',
			'refrsv_cqvalue':'Reference RSV CQ Value',
			'refrsv_interp':'Reference RSV Interpretation*',
			'refnotes':'Reference Notes',
			'reffluexcld':'Exclude?',
			}
		widgets ={
		'refflukitexp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'refflua_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refflub_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refrsv_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refflu_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;','required':True}),
			}
	def clean(self):
		models = TStg0Refflupcr1
		data = self.cleaned_data
		raw_date = data['refflu_date']
		sample = data['sample']
		kit_date = data['refflukitexp']

		find_sample = TStg0Refflupcr1.objects.filter(sample=sample).exists()
		if find_sample == True:
			print("Sample Already Exists")
			raise forms.ValidationError({'sample':'Sample {} Already Exists'.format(self.cleaned_data['sample'])})
		start_date= raw_date
		start_date = start_date.strftime("%Y-%m-%d")	
		print(start_date)
		end_date = utc.localize(datetime.datetime.now())
		end_date =end_date.strftime("%Y-%m-%d")
		print(end_date)
		print('Im here')
		if start_date > end_date:
			print('Im in the IF, should raise validation error')
			raise forms.ValidationError({'refflu_date':'Date Entered for Reference Flu Date cannot be greater than today'})
		if kit_date != None:
			kit_date = kit_date.strftime("%Y-%m-%d")
	
			if start_date > kit_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'refflukitexp':'date entered for Test Date cannot be greater than Kit Expiration Date'})

class Stg0_flu2(forms.ModelForm):
	reffluexcld=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(),label="Exclude?")#,required=False)	
	sample=forms.CharField(required=True,max_length=6, min_length=6,label="Sample ID")
	class Meta:
		model = TStg0Refflupcr2
		fields =[		
                        'refflufile_name',
			'reffluoperator',                       		
                        'refflu_date',
			'refflukitname',
			'refflukitlot',
    			'refflukitexp', 
			#'ref2_entered_by',
			#'ref2_entereddate',
			#'refflu_date', 
                        'sample', 
                        'refflua_well',
                        'refflua_cqvalue',
                        'refflua_interp',
                        'refflub_cqvalue',
                        'refflub_interp',
			'refrsv_cqvalue',
			'refrsv_interp',
                        'refnotes',
			'reffluexcld',
                        ]
		
		labels={'refflufile_name':'File Name',
			'reffluoperator':'Operator',
			'refflu_date':'Reference Date*',
			'refflukitname':'Reference Kit Name',
			'refflukitlot':'Reference Kit Lot',
			'refflukitexp':'Reference Kit Expiration',
			'sample':'Sample',
			'refflua_well':'Reference Flu A Well',
			'refflua_cqvalue':'Reference Flu A CQ Value',
			'refflua_interp':'Reference Flu A Interpretation*',
			'refflub_cqvalue':'Reference Flu B CQ Value',
			'refflub_interp':'Reference Flu B Interpretation*',
			'refrsv_cqvalue':'Reference RSV CQ Value',
			'refrsv_interp':'Reference RSV Interpretation*',
			'refnotes':'Reference Notes',
			'reffluexcld':'Exclude?',
			}
			
		widgets ={
		'refflukitexp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'refflua_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refflub_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refrsv_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refflu_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;','required':True}),
			}
	def clean(self):
		models = TStg0Refflupcr2
		data = self.cleaned_data
		raw_date = data['refflu_date']
		kit_date = data['refflukitexp']
		sample = data['sample']
		find_sample = models.objects.filter(sample=sample).exists()
		if find_sample == True:
			print("Sample Already Exists")
			raise forms.ValidationError({'sample':'Sample {} Already Exists'.format(self.cleaned_data['sample'])})
		start_date= raw_date
		start_date = start_date.strftime("%Y-%m-%d")	
		print(start_date)
		end_date = utc.localize(datetime.datetime.now())
		end_date =end_date.strftime("%Y-%m-%d")
		print(end_date)
		print('Im here')
		if start_date > end_date:
			print('Im in the IF, should raise validation error')
			raise forms.ValidationError({'refflu_date':'Date Entered for Reference Flu Date cannot be greater than today'})
		if kit_date != None:
			kit_date = kit_date.strftime("%Y-%m-%d")
	
			if start_date > kit_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'refflukitexp':'date entered for Test Date cannot be greater than Kit Expiration Date'})


class Stg1_Flu_Update(forms.ModelForm):
	excl_flag=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(),label="Exclude?")#,required=False)	
	dep=forms.ChoiceField(choices=DEP,widget=forms.RadioSelect(),label="Data Entry Person",required=True)	
	sample=forms.CharField(required=True,max_length=6, min_length=6,label="Sample ID")
	
	class Meta:
		model = TStg1FlupcrUpdate
		#widgets={'excl_flag':forms.RadioSelect(attrs={"required":""}),}
		#exclude = ('post_date','userid',)
		fields =[		
                        'dep',
			'sample',
                       	'reffluoperator',
			'refflukitname',
			'refflukitlot',
			'refflukitexp',
			'refflu_date',
                        'refflua_well', 
                        'refflua_cqvalue', 
                        'refflua_well',
                        'refflua_interp',
                        'refflub_well',
                        'refflub_cqvalue',
                        'refflub_interp',
			'refrsv_cqvalue',
			'refrsv_interp',
                        'refnotes',
			'excl_flag',
                        ]
		labels={'dep':'Dep',
			'sample':'Sample',
                       	'reffluoperator':'Operator' ,
			'refflukitname':'Reference Kit Name',
			'refflukitlot':'Reference Kit Lot',
			'refflukitexp':'Reference Kit Expiration',
			'refflu_date':'Reference Date*',
			'refflua_well':'Reference Flu A Well',
			'refflua_cqvalue':'Reference Flu A CQ Value',
			'refflua_interp':'Reference Flu A Interpretation*',
			'refflub_well':'Reference Flu B Well',
			'refflub_cqvalue':'Reference Flu B CQ Value',
			'refflub_interp':'Reference Flu B Interpretation*',
			'refrsv_cqvalue':'Reference RSV CQ Value',
			'refrsv_interp':'Reference RSV Interpretation*',
			'refnotes':'Reference Notes',
			'excl_flag':'Exclude?',
			}
		widgets ={
		'refflukitexp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'refflua_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refflub_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refrsv_interp': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refflu_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;','required':True}),
			}
	def clean(self):
		model1 = TStg0Refflupcr1
		model2 = TStg0Refflupcr1
		data = self.cleaned_data
		raw_date = data['refflu_date']
		kit_date = data['refflukitexp']
		sample = data['sample']
		start_date= raw_date
		find_sample_1 = model1.objects.filter(sample=sample).exists()
		find_sample_2 = model2.objects.filter(sample=sample).exists()
		if find_sample_1 == False and find_sample_2 == False:
			print("Sample Doesn't Exists")
			raise forms.ValidationError({'sample':'Sample {} Does Not Exists'.format(self.cleaned_data['sample'])})
		start_date = start_date.strftime("%Y-%m-%d")	
		print(start_date)
		end_date = utc.localize(datetime.datetime.now())
		end_date =end_date.strftime("%Y-%m-%d")
		print(end_date)
		print('Im here')
		if start_date > end_date:
			print('Im in the IF, should raise validation error')
			raise forms.ValidationError({'refflu_date':'Date Entered for Reference Flu Date cannot be greater than today'})
		if kit_date != None:
			kit_date = kit_date.strftime("%Y-%m-%d")
	
			if start_date > kit_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'refflukitexp':'date entered for Test Date cannot be greater than Kit Expiration Date'})

class Stg1_Brpcr_Update(forms.ModelForm):
	excl_flag=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(),label="Exclude?")#,required=False)	
	sampleid=forms.CharField(required=True,max_length=6, min_length=6,label="Sample ID")

	class Meta:
		model = TStg1BrpcrUpdate
		#widgets={'excl_flag':forms.RadioSelect(attrs={"required":""}),}
		#exclude = ('post_date','userid',)
		fields =[		
    			'sampleid', 
    			'inv_site', 
    			'inv_equipment', 
    			'inv_test_name',
    			'inv_test_date', 
    			'inv_kit_name',
    			'inv_kit_lotid',
			'inv_kit_expiration_date',
    			'inv_operator',
    			'inv_well_id',
    			'inv_sarscov2_concentration',
    			'inv_infa_concentration',
    			'inv_infb_concentration',
    			'inv_rp_concentration',
    			'inv_sarscov2_interpretation',
    			'inv_infa_interpretation',
    			'inv_infb_interpretation',
    			'inv_rp_interpretation',
    			'inv_notes',
    			'excl_flag',
                        ]
		labels={#'dep':'Dep',
    			'sampleid':'Sample ID', 
    			'inv_site':'Site', 
    			'inv_equipment':'Equipment', 
    			'inv_test_name':'Test Name',
    			'inv_test_date':'Test Date*', 
    			'inv_kit_name':'Kit Name',
    			'inv_kit_lotid':'Kit Lot ID',
			'inv_kit_expiration_date':'Kit Exp Date',
    			'inv_operator':'Operator',
    			'inv_well_id':'Well ID',
    			'inv_sarscov2_concentration':'SARS-CoV-2 Cancentration',
    			'inv_infa_concentration':'InfA Concentration',
    			'inv_infb_concentration':'InfB Concentration',
    			'inv_rp_concentration':'RP Concentration',
    			'inv_sarscov2_interpretation':'SARS-CoV-2 Interp*',
    			'inv_infa_interpretation':'InfA Interp*',
    			'inv_infb_interpretation':'InfB Interp*',
    			'inv_rp_interpretation':'RP Interp*',
    			'inv_notes':'Notes',
			'excl_flag':'Exclude?',
			}
		widgets ={
		'inv_site': forms.Select(choices=SITE_CHOICES,attrs={'class':'select','required':True}),
		'inv_sarscov2_interpretation': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'inv_infa_interpretation': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'inv_infb_interpretation': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'inv_rp_interpretation': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'inv_test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;','required':True}),
		'inv_kit_expiration_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
			}
	def clean(self):
		models = TStg1Brpcr
		data = self.cleaned_data
		raw_date = data['inv_test_date']
		print('date submit?')
		print(raw_date)	
		kit_date = data['inv_kit_expiration_date']	
		sampleid = data['sampleid']
		find_sample = models.objects.filter(sampleid=sampleid).exists()
		if find_sample == False:
			print("Sample Already Exists")
			raise forms.ValidationError({'sampleid':'Sample {} Does Not Exist'.format(self.cleaned_data['sampleid'])})
		end_date = utc.localize(datetime.datetime.now())
		end_date =end_date.strftime("%Y-%m-%d")
		start_date= raw_date
		start_date = start_date.strftime("%Y-%m-%d")	
		print(end_date)
		print('Im here')
		if start_date > end_date:
			print('Im in the IF, should raise validation error')
			raise forms.ValidationError({'inv_test_date':'Date Entered for Test Date cannot be greater than today'})
		if kit_date != None:
			kit_date = kit_date.strftime("%Y-%m-%d")
	
			if start_date > kit_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'inv_kit_expiration_date':'date entered for Test Date cannot be greater than Kit Expiration Date'})

class Stg1_Ecrf_Update(forms.ModelForm):
	excl_flag=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(),label="Exclude?")#,required=False)	
	subjectid=forms.CharField(required=True,max_length=6, min_length=6, label="Sample ID")
	#incorrect_data=forms.CharField(widget=forms.HiddenInput())

	class Meta:
		model = TStg1EcrfUpdate
		fields =[		
    			'subjectid', 
    			'specimenid', 
    			'subject_age', 
    			'subject_sex', 
    			'subject_race',
    			'subject_ethnicity',
   			'collection_date', 
    			'symptom_date', 
    			'symptom_desc', 
    			'symptom_cough',
    			'symptom_conges', 
    			'symptom_rhinorrhea', 
    			'symptom_sore_throat',
    			'symptom_fever', 
    			'symptom_headache',
    			'symptom_myalgia',
    			'symptom_other', 
    			'symptom_hospitalized', 
    			'influzab_kitname', 
    			'influza_testresult',
    			'influza_ctvalue', 
    			'influzb_testresult',
    			'influzb_ctvalue',
    			'rsv_kitname',
    			'rsv_testvalue',
    			'rsv_ctvalues', 
    			'cov2_kitname', 
    			'cov2_testresult',
    			'cov2_ctvalue', 
    			'excl_flag', 
                       
                        ]
		labels={
    			'subjectid':'Subject ID', 
    			'specimenid':'Specimen ID', 
    			'subject_age':'Subject Age', 
    			'subject_sex':'Subject Sex', 
    			'subject_race':'Subject Race',
    			'subject_ethnicity':'Subject Ethnicity',
   			'collection_date':'Collection Date', 
    			'symptom_date':'Symptom Date', 
    			'symptom_desc':'Symptom Description', 
    			'symptom_cough':'Symptom Cough',
    			'symptom_conges':'Symptom Congestion', 
    			'symptom_rhinorrhea':'Symptom Rhinorrhea', 
    			'symptom_sore_throat':'Symptom Sore Throat',
    			'symptom_fever':'Symptom Fever', 
    			'symptom_headache':'Symptom Headache',
    			'symptom_myalgia':'Symptom Myalgia',
    			'symptom_other':'Symptom Other', 
    			'symptom_hospitalized':'Symptom Hospitalized', 
    			'influzab_kitname':'Flu A/B Kit', 
    			'influza_testresult':'Flu A Test Result',
    			'influza_ctvalue':'Flu A CT Value', 
    			'influzb_testresult':'Flu B Test Result ',
    			'influzb_ctvalue':'Flu B CT Value',
    			'rsv_kitname':'RSV Kit Name',
    			'rsv_testvalue':'RSV Test Value',
    			'rsv_ctvalues':'RSV CT Values', 
    			'cov2_kitname':'COV 2 Kit Name', 
    			'cov2_testresult':'COV2 Test Result',
    			'cov2_ctvalue':'COV2 CT Value', 
    			'excl_flag': 'Exclude?',

			}
		widgets ={
		'subject_sex': forms.Select(choices=SEX_CHOICES,attrs={'class':'select'}),
		'collection_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),#,'required':True}),
		'symptom_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),#,'required':True}),
			}
	def clean(self):
		data = self.cleaned_data
		models = TStg1Ecrf
		subjectid = data['subjectid']
		find_sample = models.objects.filter(subjectid=subjectid).exists()
		if find_sample == False:
			print("Sample Already Exists")
			raise forms.ValidationError({'sample':'Sample {} Already Exists'.format(self.cleaned_data['subjectid'])})
		
		collection_date = data['collection_date']
		symptom_date= data['symptom_date']
		
		end_date = utc.localize(datetime.datetime.now())
		end_date =end_date.strftime("%Y-%m-%d")
		print(end_date)
																		
		if collection_date == None:
			print('Collection Date == None')		

		
		if collection_date != None:
			collection_date = collection_date.strftime("%Y-%m-%d")	
		
			if collection_date > end_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'collection_date':'date entered for collection date cannot be greater than today'})
		if symptom_date != None:
			symptom_date= symptom_date.strftime("%Y-%m-%d")
	
			if symptom_date > end_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'symptom_date':'date entered for symptom date cannot be greater than today'})

class Stg1_Cov2_Update(forms.ModelForm):
	excl_flag=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect(),label="Exclude?",required=True)	
	sampleid=forms.CharField(required=True,max_length=6, min_length=6,label="Sample ID")

	class Meta:
		model = TStg1Cov2Update
		fields =[		
			'sampleid', 
   			'refcov2_test_name', 
    			'refcov2_test_date', 
    			'refcov2_kit_name',
    			'refcov2_kit_lotid',
    			'refcov2_kit_expiration_date',
    			'refcov2_operator', 
    			'refcov2_well_id',
    			'refcov2_n1_concentration',
    			'refcov2_n2_concentration',
    			'refcov2_rp_concentration',
    			'refcov2_n1_droplet_count',
    			'refcov2_n2_droplet_count',
    			'refcov2_rp_droplet_count',
    			'refcov2_result_interpretation',
    			'refcov2_notes',
    			'excl_flag',
                        ]
		labels={
			'sampleid':'Sample ID', 
   			'refcov2_test_name':'Reference Cov2 Test Name', 
    			'refcov2_test_date':'Reference Cov2 Test Date*', 
    			'refcov2_kit_name':'Reference Cov2 Kit Name',
    			'refcov2_kit_lotid':'Reference Cov2 Kit Lot ID',
    			'refcov2_kit_expiration_date':'Reference Cov2 Kit Exp Date',
    			'refcov2_operator':'Reference Cov2 Operator', 
    			'refcov2_well_id':'Reference Cov2 Well ID',
    			'refcov2_n1_concentration':'Reference Cov2 N1 Concentration',
    			'refcov2_n2_concentration':'Reference Cov2 N2 Concentration',
    			'refcov2_rp_concentration':'Reference Cov2 RP Concentration',
    			'refcov2_n1_droplet_count':'Reference Cov2 N1 Droplet Count',
    			'refcov2_n2_droplet_count':'Reference Cov2 N2 Droplet Count',
    			'refcov2_rp_droplet_count':'Reference Cov2 RP Droplet Count',
    			'refcov2_result_interpretation':'Reference Cov2 Result Interp*',
    			'refcov2_notes':'Reference Cov2 Notes',
    			'excl_flag':'Excluded?',
			}
		widgets ={
		'refcov2_result_interpretation': forms.Select(choices=INTERP_CHOICES,attrs={'class':'select','required':True}),
		'refcov2_test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;','required':True}),
		'refcov2_kit_expiration_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
			}
	def clean(self):
		data = self.cleaned_data
		refcov2_date = data['refcov2_test_date']
		kitexp_date = data['refcov2_kit_expiration_date']
		models = TStg1Cov2
		sampleid = data['sampleid']
		find_sample = models.objects.filter(sampleid=sampleid).exists()
		if find_sample == False:
			print("Sample Already Exists")
			raise forms.ValidationError({'sampleid':'Sample {} Does Not Exist'.format(self.cleaned_data['sampleid'])})
		end_date = utc.localize(datetime.datetime.now())
		end_date =end_date.strftime("%Y-%m-%d")
		print(end_date)
		print('Im here')

		if refcov2_date != None:
			refcov2_date = refcov2_date.strftime("%Y-%m-%d")	
			if refcov2_date > end_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'refcov2_test_date':'date entered for Reference COV2 date cannot be greater than today'})

		if kitexp_date != None:
			kitexp_date= kitexp_date.strftime("%Y-%m-%d")
			if refcov2_date > kitexp_date:
				print('im in the if, should raise validation error')
				raise forms.ValidationError({'refcov2_kit_expiration_date':'date entered for Kit Expiration Date cannot be less than Test Date'})
