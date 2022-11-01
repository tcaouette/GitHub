
from collections import Counter
from rvpsyndromic.models import TStg2Demo

import re
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
#from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin, LoginRequiredMixin 
# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import get_current_timezone
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
#from bokeh.charts import TimeSeries
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.core.properties import value
from bokeh.embed import components
from bokeh.models import DatetimeTickFormatter,ColumnDataSource, HoverTool, value, LabelSet, Legend,LinearColorMapper, BasicTicker,PrintfTickFormatter, ColorBar,DaysTicker
from django.db.models import Sum, Count
from bokeh.models.widgets import Tabs
from bokeh.transform import cumsum,factor_cmap
from bokeh.models import LabelSet,ColumnDataSource,FactorRange 
from bokeh.layouts import gridplot
#import scipy.special
#import numpy as np
import datetime
from datetime import timedelta
from collections import Counter
from django_pandas.io import read_frame
import pandas as pd
from math import pi
from bokeh.palettes import Spectral11,Spectral6,colorblind,Inferno, BuGn, brewer, Category20c,magma,d3, Category10, Dark2, viridis, all_palettes, cividis


ecrf=TStg2Demo




def gpcht_sex_race_percent():
	y = ecrf.objects.values('subjectid').count()
	male_ethnicity = ecrf.objects.filter(subject_sex='M').values('subject_race')
	female_ethnicity = ecrf.objects.filter(subject_sex='F').values('subject_race')
	male_eth_list = list(male_ethnicity)
	female_eth_list =list(female_ethnicity)	
	male_counter_dict = Counter(ethn['subject_race'] for ethn in male_eth_list)
	male_dict = dict(male_counter_dict)
	female_counter_dict = Counter(ethn['subject_race'] for ethn in female_eth_list)
	female_dict=dict(female_counter_dict)
	n_male_dict = {'male':male_dict}
	n_female_dict ={'female':female_dict}
	all_dict = {**n_male_dict,**n_female_dict}
	df = pd.DataFrame(all_dict)
	sexs = df.columns.tolist()
	races = df.index.tolist()
	male = df['male'].tolist()
	female =df['female'].tolist()
	
	male_percent =[round((x/y)*100,2) for x in male]
	female_percent =[round((x/y)*100,2) for x in female]
	ln_male_percent = len(male)
	ln_female_percent =len(female)
	if ln_male_percent > ln_female_percent:
		len_diff = ln_male_percent - ln_female_percent
		for i in range(len_diff):
			female.append(0)
	
	if ln_female_percent > ln_male_percent:
		len_diff = ln_female_percent - ln_male_percent
		for i in range(len_diff):
			male.append(0)
		
	data = {
		'race':races,
		'Male':male_percent,
		'Female':female_percent,
		}
	x = [ (r, sex) for r in races for sex in sexs]
	print(x)
	counts = sum(zip(data['Male'],data['Female']),())
	source = ColumnDataSource(data=dict(x=x,counts=counts))
	tooltips =[
		("race, Sex","@x"),
		("Percentage","@counts %"),
		]
	return x, counts, source, tooltips,sexs,races,male,female 
