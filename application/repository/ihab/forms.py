from django import forms
from ihab.models import stg1_dataentryperson_ihab_abid_1, stg1_dataentryperson_ihab_abid_2#####insert names of the class models


class DE_Form_ihab_abid_1(forms.ModelForm):
	
	
	class Meta:
		model = stg1_dataentryperson_ihab_abid_1
			
		fields =[ 
		'sample_id',
		'analyte',
		'test_date',
		'method',
		'rep',
		'lot',
		'lot_exp',
		'exc_comments',
		'misc_comments',
		'i_well_1',
		'i_well_2',
		'i_well_3',
		'i_well_4',
		'i_well_5',
		'i_well_6',
		'i_well_7',
		'i_well_8',
		'i_well_9',
		'i_well_10',
		'i_well_11',
		'e_well_1',
		'e_well_2',
		'e_well_3',
		'e_well_4',
		'e_well_5',
		'e_well_6',
		'e_well_7',
		'e_well_8',
		'e_well_9',
		'e_well_10',
		'e_well_11',
		'card_result',
		'abid_interp'
		]
		labels={
		"i_well_1":"Initial Well 1","i_well_2":"Initial Well 2","i_well_3":"Initial Well 3",
		"i_well_4":"Initial Well 4","i_well_5":"Initial Well 5","i_well_6":"Initial Well 6",
		"i_well_7":"Initial Well 7","i_well_8":"Initial Well 8","i_well_9":"Initial Well 9",
		"i_well_10":"Initial Well 10","i_well_11":"Initial Well 11",
		"e_well_1":"Edited Well 1","e_well_2":"Edited Well 2","e_well_3":"Edited Well 3",
		"e_well_4":"Edited Well 4","e_well_5":"Edited Well 5","e_well_6":"Edited Well 6",
		"e_well_7":"Edited Well 7","e_well_8":"Edited Well 8","e_well_9":"Edited Well 9",
		"e_well_10":"Edited Well 10","e_well_11":"Edited Well 11",
		"lot_exp":"Lot Expiration Date","abid_interp":"Antibody Interpretation"

		}	
		ANALYTE_CHOICES=(	#	Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3)
		("0","Select"),
		("1","Panel 11 IgG"),
		("2","Papain"),
		("3","Panel Plus 6"),
		) 
		WELL_CHOICES=(#  -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
		("0","Select"),

		("1","-"),
		("2","1+"),
		("3","2+"),
		("4","3+"),
		("5","4+"),
		("6","+-"),
		("7","DP"),
		("8","?"),
		("9","E"),
		)
		METHOD_CHOICES=(	# Method = test(1)/reference(2)/referee(3)
		("0","Select"),
		("1","test"),
		("2","reference"),
		("3","referee"),
		)
		REP_CHOICES=(	# Rep = initial(1)/repeat(2)
		("0","Select"),
		("1","initial"),
		("2","repeat"),
		)
		CARD_CHOICES=(
		("0","Select"),
		("1","Positive"),
		("2","Negative"),
		("3","Indeterminate"),
		)
		BCW_SAMPLE_CHOICES=(
		("0","Select"),
		("1","IABW001"),
		("2","IABW002"),
		("3","IABW003"),
		("4","IABW004"),
		("5","IABW005"),
		("6","IABW006"),
		("7","IABW007"),
		("8","IABW008"),
		("9","IABW009"),
		("10","IABW010"),
		("11","IABW011"),
		("12","IABW012"),
		("13","IABW013"),
		("14","IABW014"),
		("15","IABW015"),
		("16","IABW016"),
		("17","IABW017"),
		("18","IABW018"),
		("19","IABW019"),
		("20","IABW020"),
		("21","IABL001"),
		("22","IABL002"),
		("23","IABL003"),
		("24","IABL004"),
		("25","IABL005"),
		("26","IABL006"),
		("27","IABL007"),
		("28","IABL008"),
		("29","IABL009"),
		("30","IABL010"),
		("31","IABL011"),
		("32","IABL012"),
		("33","IABL013"),
		("34","IABL014"),
		("35","IABL015"),
		("36","IABL016"),
		("37","IABL017"),
		("38","IABL018"),
		("39","IABL019"),
		("40","IABL020"),
		("41","IABN001"),
		("42","IABN002"),
		("43","IABN003"),
		("44","IABN004"),
		("45","IABN005"),
		("46","IABN006"),
		("47","IABN007"),
		("48","IABN008"),
		)
		BLD_SAMPLE_CHOICES=(
		("0","Select"),
		("1","IABW001"),
		("2","IABW002"),
		("3","IABW003"),
		("4","IABW004"),
		("5","IABW005"),
		("6","IABW006"),
		("7","IABW007"),
		("8","IABW008"),
		("9","IABW009"),
		("10","IABW010"),
		("11","IABW011"),
		("12","IABW012"),
		("13","IABW013"),
		("14","IABW014"),
		("15","IABW015"),
		("16","IABW016"),
		("17","IABW017"),
		("18","IABW018"),
		("19","IABW019"),
		("20","IABW020"),
		("21","IABL001"),
		("22","IABL002"),
		("23","IABL003"),
		("24","IABL004"),
		("25","IABL005"),
		("26","IABL006"),
		("27","IABL007"),
		("28","IABL008"),
		("29","IABL009"),
		("30","IABL010"),
		("31","IABL011"),
		("32","IABL012"),
		("33","IABL013"),
		("34","IABL014"),
		("35","IABL015"),
		("36","IABL016"),
		("37","IABL017"),
		("38","IABL018"),
		("39","IABL019"),
		("40","IABL020"),
		("41","IABN001"),
		("42","IABN002"),
		("43","IABN003"),
		("44","IABN004"),
		("45","IABN005"),
		("46","IABN006"),
		("47","IABN007"),
		("48","IABN008"),
		("49","IABN009"),
		("50","IABN010"),
		("51","IABN011"),
		("52","IABN012"),
		("53","IABN013"),
		("54","IABN014"),
		("55","IABN015"),
		("56","IABN016"),
		)


		widgets ={
		'analyte': forms.Select(choices=ANALYTE_CHOICES,attrs={'class':'select'}),
		'test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'lot_exp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'method': forms.Select(choices=METHOD_CHOICES,attrs={'class':'select'}),
		'rep': forms.Select(choices=REP_CHOICES,attrs={'class':'select'}),
		'i_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'card_result': forms.Select(choices=CARD_CHOICES,attrs={'class':'select'}),
	
		}
class DE_Form_ihab_abid_2(forms.ModelForm):
	class Meta:
		model = stg1_dataentryperson_ihab_abid_2#
		fields = [
		'sample_id',
		'analyte',
		'test_date',
		'method',
		'rep',
		'lot',
		'lot_exp',
		'exc_comments',
		'misc_comments',
		'i_well_1',
		'i_well_2',
		'i_well_3',
		'i_well_4',
		'i_well_5',
		'i_well_6',
		'i_well_7',
		'i_well_8',
		'i_well_9',
		'i_well_10',
		'i_well_11',
		'e_well_1',
		'e_well_2',
		'e_well_3',
		'e_well_4',
		'e_well_5',
		'e_well_6',
		'e_well_7',
		'e_well_8',
		'e_well_9',
		'e_well_10',
		'e_well_11',
		'card_result',
		'abid_interp'
		]
		labels={
		"i_well_1":"Initial Well 1","i_well_2":"Initial Well 2","i_well_3":"Initial Well 3",
		"i_well_4":"Initial Well 4","i_well_5":"Initial Well 5","i_well_6":"Initial Well 6",
		"i_well_7":"Initial Well 7","i_well_8":"Initial Well 8","i_well_9":"Initial Well 9",
		"i_well_10":"Initial Well 10","i_well_11":"Initial Well 11",
		"e_well_1":"Edited Well 1","e_well_2":"Edited Well 2","e_well_3":"Edited Well 3",
		"e_well_4":"Edited Well 4","e_well_5":"Edited Well 5","e_well_6":"Edited Well 6",
		"e_well_7":"Edited Well 7","e_well_8":"Edited Well 8","e_well_9":"Edited Well 9",
		"e_well_10":"Edited Well 10","e_well_11":"Edited Well 11",
		"lot_exp":"Lot Expiration Date","abid_interp":"Antibody Interpretation"


		}	
		ANALYTE_CHOICES=(	#	Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3)
		("0","Select"),
		("1","Panel 11 IgG"),
		("2","Papain"),
		("3","Panel Plus 6"),
		) 
		WELL_CHOICES=(#  -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
		("0","Select"),

		("1","-"),
		("2","1+"),
		("3","2+"),
		("4","3+"),
		("5","4+"),
		("6","+-"),
		("7","DP"),
		("8","?"),
		("9","E"),
		)
		METHOD_CHOICES=(	# Method = test(1)/reference(2)/referee(3)
		("0","Select"),
		("1","test"),
		("2","reference"),
		("3","referee"),
		)
		REP_CHOICES=(	# Rep = initial(1)/repeat(2)
		("0","Select"),
		("1","initial"),
		("2","repeat"),
		)
		CARD_CHOICES=(
		("0","Select"),
		("1","Positive"),
		("2","Negative"),
		("3","Indeterminate"),
		)


		widgets ={
		'analyte': forms.Select(choices=ANALYTE_CHOICES,attrs={'class':'select'}),
		'method': forms.Select(choices=METHOD_CHOICES,attrs={'class':'select'}),
		'test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'lot_exp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'rep': forms.Select(choices=REP_CHOICES,attrs={'class':'select'}),
		'i_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'card_result': forms.Select(choices=CARD_CHOICES,attrs={'class':'select'}),
	
		}





class BCW_Primary(forms.ModelForm):
	
	
	class Meta:
		model = stg1_dataentryperson_ihab_abid_1
			
		fields =[
#		'date_inserted',
		'site_code', 
		'sample_id',
		'analyte',
		'test_date',
		'method',
		'rep',
		'lot',
		'lot_exp',
		'exc_comments',
		'misc_comments',
		'i_well_1',
		'i_well_2',
		'i_well_3',
		'i_well_4',
		'i_well_5',
		'i_well_6',
		'i_well_7',
		'i_well_8',
		'i_well_9',
		'i_well_10',
		'i_well_11',
		'e_well_1',
		'e_well_2',
		'e_well_3',
		'e_well_4',
		'e_well_5',
		'e_well_6',
		'e_well_7',
		'e_well_8',
		'e_well_9',
		'e_well_10',
		'e_well_11',
		'card_result',
		'abid_interp'
		]
		labels={
		"i_well_1":"Initial Well 1","i_well_2":"Initial Well 2","i_well_3":"Initial Well 3",
		"i_well_4":"Initial Well 4","i_well_5":"Initial Well 5","i_well_6":"Initial Well 6",
		"i_well_7":"Initial Well 7","i_well_8":"Initial Well 8","i_well_9":"Initial Well 9",
		"i_well_10":"Initial Well 10","i_well_11":"Initial Well 11",
		"e_well_1":"Edited Well 1","e_well_2":"Edited Well 2","e_well_3":"Edited Well 3",
		"e_well_4":"Edited Well 4","e_well_5":"Edited Well 5","e_well_6":"Edited Well 6",
		"e_well_7":"Edited Well 7","e_well_8":"Edited Well 8","e_well_9":"Edited Well 9",
		"e_well_10":"Edited Well 10","e_well_11":"Edited Well 11",
		"lot_exp":"Lot Expiration Date","abid_interp":"Antibody Interpretation","exc_comments":"Exclusion Comments"


		}
		SITE_CHOICES=(
		("bcw","BCW"),
		)	
		ANALYTE_CHOICES=(	#	Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3)
		("0","Select"),
		("1","Anti-D"),
		("2","Anti-C"),
		("4","Anti-E"),
		("5","Anti-c"),
		("6","Anti-e"),
		("7","Anti-Jka"),
		("8","Anti-Jkb"),
		("9","Anti-S"),
		("10","Anti-s"),
		("11","Anti-K"),
		("12","Anti-k"),
		("13","Anti-Kpa"),
		("14","Anti-Kpb"),
		("15","Anti-Fya"),
		("16","Anti-Fyb"),
		) 
		WELL_CHOICES=(#  -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
		("0","Select"),

		("1","-"),
		("2","1+"),
		("3","2+"),
		("4","3+"),
		("5","4+"),
		("6","+-"),
		("7","DP"),
		("8","?"),
		("9","E"),
		)
		METHOD_CHOICES=(	# Method = test(1)/reference(2)/referee(3)
		("0","Select"),
		("1","Panel 11 IgG"),
		("2","Panel Plus 6"),
	
		)
		REP_CHOICES=(	# Rep = initial(1)/repeat(2)
		("0","Select"),
		("1","initial"),
		("2","repeat"),
		)
		CARD_CHOICES=(
		("0","Select"),
		("1","Positive"),
		("2","Negative"),
		("3","Indeterminate"),
		)
		BCW_SAMPLE_CHOICES=(
		("0","Select"),
		("1","IABW001"),
		("2","IABW002"),
		("3","IABW003"),
		("4","IABW004"),
		("5","IABW005"),
		("6","IABW006"),
		("7","IABW007"),
		("8","IABW008"),
		("9","IABW009"),
		("10","IABW010"),
		("11","IABW011"),
		("12","IABW012"),
		("13","IABW013"),
		("14","IABW014"),
		("15","IABW015"),
		("16","IABW016"),
		("17","IABW017"),
		("18","IABW018"),
		("19","IABW019"),
		("20","IABW020"),
		("21","IABL001"),
		("22","IABL002"),
		("23","IABL003"),
		("24","IABL004"),
		("25","IABL005"),
		("26","IABL006"),
		("27","IABL007"),
		("28","IABL008"),
		("29","IABL009"),
		("30","IABL010"),
		("31","IABL011"),
		("32","IABL012"),
		("33","IABL013"),
		("34","IABL014"),
		("35","IABL015"),
		("36","IABL016"),
		("37","IABL017"),
		("38","IABL018"),
		("39","IABL019"),
		("40","IABL020"),
		("41","IABN001"),
		("42","IABN002"),
		("43","IABN003"),
		("44","IABN004"),
		("45","IABN005"),
		("46","IABN006"),
		("47","IABN007"),
		("48","IABN008"),
		)


		widgets ={
		'site_code': forms.Select(choices=SITE_CHOICES,attrs={'class':'select'}),
		'sample_id': forms.Select(choices=BCW_SAMPLE_CHOICES,attrs={'class':'select'}),
		'analyte': forms.Select(choices=ANALYTE_CHOICES,attrs={'class':'select'}),
		'test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'lot_exp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'method': forms.Select(choices=METHOD_CHOICES,attrs={'class':'select'}),
		'rep': forms.Select(choices=REP_CHOICES,attrs={'class':'select'}),
		'i_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'card_result': forms.Select(choices=CARD_CHOICES,attrs={'class':'select'}),
	
		}


class BCW_Secondary(forms.ModelForm):
	class Meta:
		model = stg1_dataentryperson_ihab_abid_2#tg1_dataentryperson_ihab_abid_1
		fields = [
		'site_code', 
		'sample_id',
		'analyte',
		'test_date',
		'method',
		'rep',
		'lot',
		'lot_exp',
		'exc_comments',
		'misc_comments',
		'i_well_1',
		'i_well_2',
		'i_well_3',
		'i_well_4',
		'i_well_5',
		'i_well_6',
		'i_well_7',
		'i_well_8',
		'i_well_9',
		'i_well_10',
		'i_well_11',
		'e_well_1',
		'e_well_2',
		'e_well_3',
		'e_well_4',
		'e_well_5',
		'e_well_6',
		'e_well_7',
		'e_well_8',
		'e_well_9',
		'e_well_10',
		'e_well_11',
		'card_result',
		'abid_interp'
		]
		labels={
		"i_well_1":"Initial Well 1","i_well_2":"Initial Well 2","i_well_3":"Initial Well 3",
		"i_well_4":"Initial Well 4","i_well_5":"Initial Well 5","i_well_6":"Initial Well 6",
		"i_well_7":"Initial Well 7","i_well_8":"Initial Well 8","i_well_9":"Initial Well 9",
		"i_well_10":"Initial Well 10","i_well_11":"Initial Well 11",
		"e_well_1":"Edited Well 1","e_well_2":"Edited Well 2","e_well_3":"Edited Well 3",
		"e_well_4":"Edited Well 4","e_well_5":"Edited Well 5","e_well_6":"Edited Well 6",
		"e_well_7":"Edited Well 7","e_well_8":"Edited Well 8","e_well_9":"Edited Well 9",
		"e_well_10":"Edited Well 10","e_well_11":"Edited Well 11",
		"lot_exp":"Lot Expiration Date","abid_interp":"Antibody Interpretation","exc_comments":"Exclusion Comments"


		}	
		SITE_CHOICES=(
		("bcw","BCW"),
		)	
		ANALYTE_CHOICES=(	#	Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3)
		("0","Select"),
		("1","Anti-D"),
		("2","Anti-C"),
		("4","Anti-E"),
		("5","Anti-c"),
		("6","Anti-e"),
		("7","Anti-Jka"),
		("8","Anti-Jkb"),
		("9","Anti-S"),
		("10","Anti-s"),
		("11","Anti-K"),
		("12","Anti-k"),
		("13","Anti-Kpa"),
		("14","Anti-Kpb"),
		("15","Anti-Fya"),
		("16","Anti-Fyb"),
		) 
		WELL_CHOICES=(#  -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
		("0","Select"),

		("1","-"),
		("2","1+"),
		("3","2+"),
		("4","3+"),
		("5","4+"),
		("6","+-"),
		("7","DP"),
		("8","?"),
		("9","E"),
		)
		METHOD_CHOICES=(	# Method = test(1)/reference(2)/referee(3)
		("0","Select"),
		("1","Panel 11 IgG"),
		("2","Panel Plus 6"),
		
		)
		REP_CHOICES=(	# Rep = initial(1)/repeat(2)
		("0","Select"),
		("1","initial"),
		("2","repeat"),
		)
		CARD_CHOICES=(
		("0","Select"),
		("1","Positive"),
		("2","Negative"),
		("3","Indeterminate"),
		)
 	
		BCW_SAMPLE_CHOICES=(
		("0","Select"),
		("1","IABW001"),
		("2","IABW002"),
		("3","IABW003"),
		("4","IABW004"),
		("5","IABW005"),
		("6","IABW006"),
		("7","IABW007"),
		("8","IABW008"),
		("9","IABW009"),
		("10","IABW010"),
		("11","IABW011"),
		("12","IABW012"),
		("13","IABW013"),
		("14","IABW014"),
		("15","IABW015"),
		("16","IABW016"),
		("17","IABW017"),
		("18","IABW018"),
		("19","IABW019"),
		("20","IABW020"),
		("21","IABL001"),
		("22","IABL002"),
		("23","IABL003"),
		("24","IABL004"),
		("25","IABL005"),
		("26","IABL006"),
		("27","IABL007"),
		("28","IABL008"),
		("29","IABL009"),
		("30","IABL010"),
		("31","IABL011"),
		("32","IABL012"),
		("33","IABL013"),
		("34","IABL014"),
		("35","IABL015"),
		("36","IABL016"),
		("37","IABL017"),
		("38","IABL018"),
		("39","IABL019"),
		("40","IABL020"),
		("41","IABN001"),
		("42","IABN002"),
		("43","IABN003"),
		("44","IABN004"),
		("45","IABN005"),
		("46","IABN006"),
		("47","IABN007"),
		("48","IABN008"),
		)


		widgets ={
		'site_code': forms.Select(choices=SITE_CHOICES,attrs={'class':'select'}),
		'sample_id': forms.Select(choices=BCW_SAMPLE_CHOICES,attrs={'class':'select'}),
		'analyte': forms.Select(choices=ANALYTE_CHOICES,attrs={'class':'select'}),
		'method': forms.Select(choices=METHOD_CHOICES,attrs={'class':'select'}),
		'test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'lot_exp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'rep': forms.Select(choices=REP_CHOICES,attrs={'class':'select'}),
		'i_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'card_result': forms.Select(choices=CARD_CHOICES,attrs={'class':'select'}),
	
		}

class BLD_Primary(forms.ModelForm):
	
	
	class Meta:
		model = stg1_dataentryperson_ihab_abid_1
			
		fields =[ 
		'site_code', 
		'sample_id',
		'analyte',
		'test_date',
		'method',
		'rep',
		'lot',
		'lot_exp',
		'exc_comments',
		'misc_comments',
		'i_well_1',
		'i_well_2',
		'i_well_3',
		'i_well_4',
		'i_well_5',
		'i_well_6',
		'i_well_7',
		'i_well_8',
		'i_well_9',
		'i_well_10',
		'i_well_11',
		'e_well_1',
		'e_well_2',
		'e_well_3',
		'e_well_4',
		'e_well_5',
		'e_well_6',
		'e_well_7',
		'e_well_8',
		'e_well_9',
		'e_well_10',
		'e_well_11',
		'card_result',
		'abid_interp'
		]
		labels={
		"i_well_1":"Initial Well 1","i_well_2":"Initial Well 2","i_well_3":"Initial Well 3",
		"i_well_4":"Initial Well 4","i_well_5":"Initial Well 5","i_well_6":"Initial Well 6",
		"i_well_7":"Initial Well 7","i_well_8":"Initial Well 8","i_well_9":"Initial Well 9",
		"i_well_10":"Initial Well 10","i_well_11":"Initial Well 11",
		"e_well_1":"Edited Well 1","e_well_2":"Edited Well 2","e_well_3":"Edited Well 3",
		"e_well_4":"Edited Well 4","e_well_5":"Edited Well 5","e_well_6":"Edited Well 6",
		"e_well_7":"Edited Well 7","e_well_8":"Edited Well 8","e_well_9":"Edited Well 9",
		"e_well_10":"Edited Well 10","e_well_11":"Edited Well 11",

		"lot_exp":"Lot Expiration Date","abid_interp":"Antibody Interpretation","exc_comments":"Exclusion Comments"


		}	
		ANALYTE_CHOICES=(	#	Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3)
		("0","Select"),
		("1","Anti-D"),
		("2","Anti-C"),
		("4","Anti-E"),
		("5","Anti-c"),
		("6","Anti-e"),
		("7","Anti-Jka"),
		("8","Anti-Jkb"),
		("9","Anti-S"),
		("10","Anti-s"),
		("11","Anti-K"),
		("12","Anti-k"),
		("13","Anti-Kpa"),
		("14","Anti-Kpb"),
		("15","Anti-Fya"),
		("16","Anti-Fyb"),
		) 
		WELL_CHOICES=(#  -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
		("0","Select"),

		("1","-"),
		("2","1+"),
		("3","2+"),
		("4","3+"),
		("5","4+"),
		("6","+-"),
		("7","DP"),
		("8","?"),
		("9","E"),
		)
		METHOD_CHOICES=(	# Method = test(1)/reference(2)/referee(3)
		("0","Select"),
		("1","Panel 11 IgG"),
		("2","Panel Plus 6"),
		
		)
		REP_CHOICES=(	# Rep = initial(1)/repeat(2)
		("0","Select"),
		("1","initial"),
		("2","repeat"),
		)
		CARD_CHOICES=(
		("0","Select"),
		("1","Positive"),
		("2","Negative"),
		("3","Indeterminate"),
		)
		BLD_SAMPLE_CHOICES=(
		("0","Select"),
		("1","IABW001"),
		("2","IABW002"),
		("3","IABW003"),
		("4","IABW004"),
		("5","IABW005"),
		("6","IABW006"),
		("7","IABW007"),
		("8","IABW008"),
		("9","IABW009"),
		("10","IABW010"),
		("11","IABW011"),
		("12","IABW012"),
		("13","IABW013"),
		("14","IABW014"),
		("15","IABW015"),
		("16","IABW016"),
		("17","IABW017"),
		("18","IABW018"),
		("19","IABW019"),
		("20","IABW020"),
		("21","IABL001"),
		("22","IABL002"),
		("23","IABL003"),
		("24","IABL004"),
		("25","IABL005"),
		("26","IABL006"),
		("27","IABL007"),
		("28","IABL008"),
		("29","IABL009"),
		("30","IABL010"),
		("31","IABL011"),
		("32","IABL012"),
		("33","IABL013"),
		("34","IABL014"),
		("35","IABL015"),
		("36","IABL016"),
		("37","IABL017"),
		("38","IABL018"),
		("39","IABL019"),
		("40","IABL020"),
		("41","IABN001"),
		("42","IABN002"),
		("43","IABN003"),
		("44","IABN004"),
		("45","IABN005"),
		("46","IABN006"),
		("47","IABN007"),
		("48","IABN008"),
		("49","IABN009"),
		("50","IABN010"),
		("51","IABN011"),
		("52","IABN012"),
		("53","IABN013"),
		("54","IABN014"),
		("55","IABN015"),
		("56","IABN016"),
		)
		SITE_CHOICES=(
		("bld","BLD"),
		)	


		widgets ={
		'site_code': forms.Select(choices=SITE_CHOICES,attrs={'class':'select'}),
		'sample_id': forms.Select(choices=BLD_SAMPLE_CHOICES,attrs={'class':'select'}),
		'analyte': forms.Select(choices=ANALYTE_CHOICES,attrs={'class':'select'}),
		'test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'lot_exp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'method': forms.Select(choices=METHOD_CHOICES,attrs={'class':'select'}),
		'rep': forms.Select(choices=REP_CHOICES,attrs={'class':'select'}),
		'i_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'card_result': forms.Select(choices=CARD_CHOICES,attrs={'class':'select'}),
	
		}

class BLD_Secondary(forms.ModelForm):
	
	
	class Meta:
		model = stg1_dataentryperson_ihab_abid_2#tg1_dataentryperson_ihab_abid_1
			
		fields =[
		'site_code', 
		'sample_id',
		'analyte',
		'test_date',
		'method',
		'rep',
		'lot',
		'lot_exp',
		'exc_comments',
		'misc_comments',
		'i_well_1',
		'i_well_2',
		'i_well_3',
		'i_well_4',
		'i_well_5',
		'i_well_6',
		'i_well_7',
		'i_well_8',
		'i_well_9',
		'i_well_10',
		'i_well_11',
		'e_well_1',
		'e_well_2',
		'e_well_3',
		'e_well_4',
		'e_well_5',
		'e_well_6',
		'e_well_7',
		'e_well_8',
		'e_well_9',
		'e_well_10',
		'e_well_11',
		'card_result',
		'abid_interp'
		]
		labels={
		"i_well_1":"Initial Well 1","i_well_2":"Initial Well 2","i_well_3":"Initial Well 3",
		"i_well_4":"Initial Well 4","i_well_5":"Initial Well 5","i_well_6":"Initial Well 6",
		"i_well_7":"Initial Well 7","i_well_8":"Initial Well 8","i_well_9":"Initial Well 9",
		"i_well_10":"Initial Well 10","i_well_11":"Initial Well 11",
		"e_well_1":"Edited Well 1","e_well_2":"Edited Well 2","e_well_3":"Edited Well 3",
		"e_well_4":"Edited Well 4","e_well_5":"Edited Well 5","e_well_6":"Edited Well 6",
		"e_well_7":"Edited Well 7","e_well_8":"Edited Well 8","e_well_9":"Edited Well 9",
		"e_well_10":"Edited Well 10","e_well_11":"Edited Well 11",
		"lot_exp":"Lot Expiration Date","abid_interp":"Antibody Interpretation","exc_comments":"Exclusion Comments"


		}	
		ANALYTE_CHOICES=(	#	Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3)
		("0","Select"),
		("1","Anti-D"),
		("2","Anti-C"),
		("4","Anti-E"),
		("5","Anti-c"),
		("6","Anti-e"),
		("7","Anti-Jka"),
		("8","Anti-Jkb"),
		("9","Anti-S"),
		("10","Anti-s"),
		("11","Anti-K"),
		("12","Anti-k"),
		("13","Anti-Kpa"),
		("14","Anti-Kpb"),
		("15","Anti-Fya"),
		("16","Anti-Fyb"),
		) 
		WELL_CHOICES=(#  -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
		("0","Select"),

		("1","-"),
		("2","1+"),
		("3","2+"),
		("4","3+"),
		("5","4+"),
		("6","+-"),
		("7","DP"),
		("8","?"),
		("9","E"),
		)
		METHOD_CHOICES=(	# Method = test(1)/reference(2)/referee(3)
		("0","Select"),
		("1","Panel 11 IgG"),
		("2","Panel Plus 6"),
		
		)
		REP_CHOICES=(	# Rep = initial(1)/repeat(2)
		("0","Select"),
		("1","initial"),
		("2","repeat"),
		)
		CARD_CHOICES=(
		("0","Select"),
		("1","Positive"),
		("2","Negative"),
		("3","Indeterminate"),
		)
		BLD_SAMPLE_CHOICES=(
		("0","Select"),
		("1","IABW001"),
		("2","IABW002"),
		("3","IABW003"),
		("4","IABW004"),
		("5","IABW005"),
		("6","IABW006"),
		("7","IABW007"),
		("8","IABW008"),
		("9","IABW009"),
		("10","IABW010"),
		("11","IABW011"),
		("12","IABW012"),
		("13","IABW013"),
		("14","IABW014"),
		("15","IABW015"),
		("16","IABW016"),
		("17","IABW017"),
		("18","IABW018"),
		("19","IABW019"),
		("20","IABW020"),
		("21","IABL001"),
		("22","IABL002"),
		("23","IABL003"),
		("24","IABL004"),
		("25","IABL005"),
		("26","IABL006"),
		("27","IABL007"),
		("28","IABL008"),
		("29","IABL009"),
		("30","IABL010"),
		("31","IABL011"),
		("32","IABL012"),
		("33","IABL013"),
		("34","IABL014"),
		("35","IABL015"),
		("36","IABL016"),
		("37","IABL017"),
		("38","IABL018"),
		("39","IABL019"),
		("40","IABL020"),
		("41","IABN001"),
		("42","IABN002"),
		("43","IABN003"),
		("44","IABN004"),
		("45","IABN005"),
		("46","IABN006"),
		("47","IABN007"),
		("48","IABN008"),
		("49","IABN009"),
		("50","IABN010"),
		("51","IABN011"),
		("52","IABN012"),
		("53","IABN013"),
		("54","IABN014"),
		("55","IABN015"),
		("56","IABN016"),
		)
		SITE_CHOICES=(
		("bld","BLD"),
		)	


		widgets ={
		'site_code': forms.Select(choices=SITE_CHOICES,attrs={'class':'select'}),
		'sample_id': forms.Select(choices=BLD_SAMPLE_CHOICES,attrs={'class':'select'}),
		'analyte': forms.Select(choices=ANALYTE_CHOICES,attrs={'class':'select'}),
		'test_date': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'lot_exp': forms.SelectDateWidget(attrs={'style':'display: inline-block; width:auto;'}),
		'method': forms.Select(choices=METHOD_CHOICES,attrs={'class':'select'}),
		'rep': forms.Select(choices=REP_CHOICES,attrs={'class':'select'}),
		'i_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'i_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_1': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_2': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_3': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_4': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_5': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_6': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_7': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_8': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_9': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_10': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'e_well_11': forms.Select(choices=WELL_CHOICES,attrs={'class':'select'}),
		'card_result': forms.Select(choices=CARD_CHOICES,attrs={'class':'select'}),
	
		}
