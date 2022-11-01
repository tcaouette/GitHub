from collections import Counter
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy, reverse
from rvpsyndromic.models import TStg0Brpcr, TStg0Ecrf, TStg0Refcov2Pcr1, TStg0Refcov2Pcr2, TStg0Refflupcr1, TStg0Refflupcr2, TStg1Brpcr, TStg1Cov2, TStg1Ecrf, EcrfExclusionTrans,BrpcrExclusionTrans,Stg1Cov2PcrExclTrans,Stg1RefflupcrExclTrans,TStg1FlupcrUpdate,TStg1ReffluMismatch,TStg1ReffluMatch,TStg1BrpcrUpdate,TStg1EcrfUpdate,TStg1Cov2Update,TStg2Ad,TStg2Subjexcl,TStg2Demo

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
import scipy.special
import numpy as np
import datetime
from datetime import timedelta
from collections import Counter
from django_pandas.io import read_frame
import pandas as pd
from math import pi
from bokeh.palettes import Spectral11,Spectral6,colorblind,Inferno, BuGn, brewer, Category20c,magma,d3, Category10, Dark2, viridis, all_palettes, cividis


'''

Metrics Views for comupting and displaying pre-defined metrics

'''

ecrf=TStg2Demo


def percent_samples_in(request):
	y = ecrf.objects.values('subjectid').count()
	percent_in = (y/400)*100
	count_in = y
	male_sex = ecrf.objects.filter(subject_sex = 'M').count()
	female_sex =ecrf.objects.filter(subject_sex = 'F').count()
	percent_male = round((male_sex/y)*100,2)
	percent_female = round((female_sex/y)*100,2)
	print(percent_male)
	print(percent_female)
	print(percent_male + percent_female)
	chart_colors=['#44e5e2','#e29e44']
	pie = {
		'male':percent_male,
		'female':percent_female,
		}	
	color_num = len(pie)
	data = pd.Series(pie).reset_index(name='value').rename(columns={'index':'percent_sex'})
	data['angle'] = (data['value']/data['value'].sum()) * (2*pi)
	data['color'] = chart_colors[:color_num]
	p = figure(
		plot_height=350,
		title="Percentage Sex",
		tooltips="@percent_sex: @value%",x_range=(-0.5,1.0))
	p.wedge(x=0,y=1,radius=0.4,
		start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
		line_color = "white",color='color',legend='percent_sex', source=data)

	data["value"] = data['value'].astype(str)
	data["value"] = data["value"].str.pad(35,side="left")
	print(data)
	source = ColumnDataSource(data)
	print(source)
	labels = LabelSet(x=0,y=1, text = 'value',
				angle=cumsum('angle',include_zero=True),
				source = source, render_mode='canvas')
	p.add_layout(labels)
	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color=None
	#p.line(x,y,legend='f(x)',line_width=2)
	show(p)
	script, div1=components(p)
	context={'script':script,'div1':div1,'percent_in':round(percent_in,2), 'count_in':count_in}
	return context

def ethnicity_count(request):
	y = ecrf.objects.values('subject_ethnicity').count()
	eth = ecrf.objects.values('subject_ethnicity')
	eth_list=list(eth)
	ethnicity_dict = Counter(ethn['subject_ethnicity'] for ethn in eth_list)
	eth_dict=dict(ethnicity_dict)
	percent_eth = {k: round((v/y)*100) for k, v in eth_dict.items()} 
	print(percent_eth)#eth_dict={}
	#for i in eth_list:
	#	eth_dict.update(i)
	#print(eth_dict)
	
	chart_colors=['#44e5e2','#e29e44']
	pie = {
	#	'':,
	#	'':,
		}	
	color_num = len(pie)
	data = pd.Series(ethnicity_dict).reset_index(name='value').rename(columns={'index':'ethnicity'})
	data['angle'] = (data['value']/data['value'].sum()) * (2*pi)
	colours = viridis(len(eth_dict)) 
	print(colours)
	data['color'] = colours #chart_colors[:color_num]
	p = figure(
		plot_height=350,
		title="Counts of Ethnicities",
		tooltips="@ethnicity: @value",x_range=(-0.5,1.0))
	p.wedge(x=0,y=1,radius=0.4,
		start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
		line_color = "white",color='color',legend='ethnicity', source=data)

	data["value"] = data['value'].astype(str)
	data["value"] = data["value"].str.pad(35,side="left")
	print(data)
	source = ColumnDataSource(data)
	print(source)
	labels = LabelSet(x=0,y=1, text = 'value',
				angle=cumsum('angle',include_zero=True),
				source = source, render_mode='canvas')
	p.add_layout(labels)
	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color=None
	#p.line(x,y,legend='f(x)',line_width=2)
	show(p)
	script, div2=components(p)
	context={'script2':script,'div2':div2}
	return context

def ethnicity_percent(request):
	y = ecrf.objects.values('subject_ethnicity').count()
	eth = ecrf.objects.values('subject_ethnicity')
	eth_list=list(eth)
	ethnicity_dict = Counter(ethn['subject_ethnicity'] for ethn in eth_list)
	eth_dict=dict(ethnicity_dict)
	percent_eth = {k: round((v/y)*100) for k, v in eth_dict.items()} 
	print(percent_eth)#eth_dict={}
	#for i in eth_list:
	#	eth_dict.update(i)
	#print(eth_dict)
	
	chart_colors=['#44e5e2','#e29e44']
	pie = {
	#	'':,
	#	'':,
		}	
	color_num = len(pie)
	data = pd.Series(percent_eth).reset_index(name='value').rename(columns={'index':'ethnicity'})
	data['angle'] = (data['value']/data['value'].sum()) * (2*pi)
	colours = cividis(len(eth_dict)) 
	print(colours)
	data['color'] = colours #chart_colors[:color_num]
	p = figure(
		plot_height=350,
		title="Percent of Ethnicities",
		tooltips="@ethnicity: @value %",x_range=(-0.5,1.0))
	p.wedge(x=0,y=1,radius=0.4,
		start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
		line_color = "white",color='color',legend='ethnicity', source=data)

	data["value"] = data['value'].astype(str)
	data["value"] = data["value"].str.pad(35,side="left")
	print(data)
	source = ColumnDataSource(data)
	print(source)
	labels = LabelSet(x=0,y=1, text = 'value',
				angle=cumsum('angle',include_zero=True),
				source = source, render_mode='canvas')
	p.add_layout(labels)
	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color=None
	#p.line(x,y,legend='f(x)',line_width=2)
	show(p)
	script, div3=components(p)
	context={'script3':script,'div3':div3}
	return context

def sex_ethnicity_count(request):
	y = ecrf.objects.values('subject_ethnicity').count()
	male_ethnicity = ecrf.objects.filter(subject_sex='M').values('subject_ethnicity')
	female_ethnicity = ecrf.objects.filter(subject_sex='F').values('subject_ethnicity')
	male_eth_list = list(male_ethnicity)
	female_eth_list =list(female_ethnicity)	
	male_counter_dict = Counter(ethn['subject_ethnicity'] for ethn in male_eth_list)
	male_dict = dict(male_counter_dict)
	female_counter_dict = Counter(ethn['subject_ethnicity'] for ethn in female_eth_list)
	female_dict=dict(female_counter_dict)
	m_list_values = list(male_dict.values())
	f_list_values = list(female_dict.values())
	#m_f_dict = {**male_dict,**female_dict}
	#percent_eth = {k: round((v/y)*100) for k, v in eth_dict.items()} 
	print(m_list_values)
	print(f_list_values)
	n_male_dict = {'male':male_dict}
	n_female_dict ={'female':female_dict}
	all_dict = {**n_male_dict,**n_female_dict}
	print(all_dict)
	df = pd.DataFrame(all_dict)
	print(df)
	sexs = df.columns.tolist()
	ethnicity = df.index.tolist()
	#print(m_f)
	#print(ethnicity)
	data = {
		'Ethnicities':ethnicity,
		'Male':m_list_values,
		'Female':f_list_values,
		}
	x = [ (ethn, sex) for ethn in ethnicity for sex in sexs]
	counts = sum(zip(data['Male'],data['Female']),())
	source = ColumnDataSource(data=dict(x=x,counts=counts))
	tooltips =[
		("Ethnicity, Sex","@x"),
		("Total","@counts"),
	]

	p = figure(x_range=FactorRange(*x), plot_height=350, title="Ethnicity Counts by Sex",
		toolbar_location="right", tools="hover",tooltips=tooltips
		)
	p.vbar(x='x', top='counts', width=0.9, source = source, line_color="white",
		fill_color=factor_cmap('x', palette=Spectral11, factors=sexs, start =1, end=2))
	p.y_range.start=0
	p.x_range.range_padding=0.1
	p.xaxis.major_label_orientation=1
	p.xgrid.grid_line_color=None		
				
	
	script, div4=components(p)
	context={'script4':script,'div4':div4}
	#context=None	
	return context

def sex_ethnicity_percent(request):
	y = ecrf.objects.values('subject_ethnicity').count()
	male_ethnicity = ecrf.objects.filter(subject_sex='M').values('subject_ethnicity')
	female_ethnicity = ecrf.objects.filter(subject_sex='F').values('subject_ethnicity')
	male_eth_list = list(male_ethnicity)
	female_eth_list =list(female_ethnicity)	
	male_counter_dict = Counter(ethn['subject_ethnicity'] for ethn in male_eth_list)
	male_dict = dict(male_counter_dict)
	female_counter_dict = Counter(ethn['subject_ethnicity'] for ethn in female_eth_list)
	female_dict=dict(female_counter_dict)
	m_list_values = list(male_dict.values())
	f_list_values = list(female_dict.values())
	male_percent =[round((x/y)*100,2) for x in m_list_values]
	female_percent =[round((x/y)*100,2) for x in f_list_values]
	n_male_dict = {'male':male_dict}
	n_female_dict ={'female':female_dict}
	all_dict = {**n_male_dict,**n_female_dict}
	df = pd.DataFrame(all_dict)
	sexs = df.columns.tolist()
	ethnicity = df.index.tolist()
	data = {
		'Ethnicities':ethnicity,
		'Male':male_percent,
		'Female':female_percent,
		}
	x = [ (ethn, sex) for ethn in ethnicity for sex in sexs]
	counts = sum(zip(data['Male'],data['Female']),())
	source = ColumnDataSource(data=dict(x=x,counts=counts))
	tooltips =[
		("Ethnicity, Sex","@x"),
		("Percentage","@counts %"),
	]
	p = figure(x_range=FactorRange(*x), plot_height=350, title="Ethnicity Percentage by Sex",
			toolbar_location="right", tools="hover",tooltips=tooltips)
	p.vbar(x='x', top='counts', width=0.9, source = source, line_color="white",
		fill_color=factor_cmap('x', palette=Spectral6, factors=sexs, start =1, end=2))
	p.y_range.start=0
	p.x_range.range_padding=0.1
	p.xaxis.major_label_orientation=1
	p.xgrid.grid_line_color=None		
				
	
	script, div5=components(p)
	context={'script5':script,'div5':div5}
	#context=None	
	return context

def symptom_counts_cov_pos(request):
	symptoms = ecrf.objects.filter(cov2_testresult='Positive').values('symptom_cough','symptom_conges','symptom_rhinorrhea','symptom_sore_throat','symptom_fever', 'symptom_headache','symptom_myalgia')
	symptoms_list =list(symptoms)
	symptoms_df = pd.DataFrame(symptoms_list)
	int_df = symptoms_df.replace(to_replace=['Yes','No'],value=[1,0])
	counts = Counter()
	symp_dict = int_df.to_dict()
	result ={}
	counts=Counter()
	symp_dict_list=[]
	symp_dict_list.append(symp_dict)
	for i in symp_dict_list:
		for k,v in i.items():
			counts[k]+=sum(v.values())
	symptom_counts = dict(counts)
		
	data = pd.Series(symptom_counts).reset_index(name='value').rename(columns={'index':'symptom_counts'})
	data['angle'] = (data['value']/data['value'].sum()) * (2*pi)
	data['color'] = magma(len(symptom_counts)) 
	p = figure(
		plot_height=350,
		title="Symptom Counts for COVID-19 POSITIVE",
		tooltips="@symptom_counts: @value",x_range=(-0.5,1.0))
	p.wedge(x=0,y=1,radius=0.4,
		start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
		line_color = "white",color='color',legend='symptom_counts', source=data)

	data["value"] = data['value'].astype(str)
	data["value"] = data["value"].str.pad(35,side="left")
	source = ColumnDataSource(data)
	labels = LabelSet(x=0,y=1, text = 'value',
				angle=cumsum('angle',include_zero=True),
				source = source, render_mode='canvas')
	p.add_layout(labels)
	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color=None
	
	script, div6=components(p)
	context={'script6':script,'div6':div6}
	return context	

def sex_race_percent(request):
	y = ecrf.objects.values('subjectid').count()
	male_ethnicity = ecrf.objects.filter(subject_sex='M').values('subject_race')
	female_ethnicity = ecrf.objects.filter(subject_sex='F').values('subject_race')
	male_eth_list = list(male_ethnicity)
	female_eth_list =list(female_ethnicity)	
	male_counter_dict = Counter(ethn['subject_race'] for ethn in male_eth_list)
	male_dict = dict(male_counter_dict)
	female_counter_dict = Counter(ethn['subject_race'] for ethn in female_eth_list)
	female_dict=dict(female_counter_dict)
	m_list_values = list(male_dict.values())
	f_list_values = list(female_dict.values())
	male_percent =[round((x/y)*100,2) for x in m_list_values]
	female_percent =[round((x/y)*100,2) for x in f_list_values]
	print(male_percent)
	print(female_percent)
	n_male_dict = {'male':male_dict}
	n_female_dict ={'female':female_dict}
	all_dict = {**n_male_dict,**n_female_dict}
	df = pd.DataFrame(all_dict)
	sexs = df.columns.tolist()
	races = df.index.tolist()
	print(races)
	print(male_percent)
	print(female_percent)	
	ln_male_percent = len(male_percent)
	ln_female_percent =len(female_percent)
	if ln_male_percent > ln_female_percent:
		len_diff = ln_male_percent - ln_female_percent
		for i in range(len_diff):
			female_percent.append(0)
	
	if ln_female_percent > ln_male_percent:
		len_diff = ln_female_percent - ln_male_percent
		for i in range(len_diff):
			male_percent.append(0)
		
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
	p = figure(x_range=FactorRange(*x), plot_height=350, title="Race Percentage by Sex",
			toolbar_location="right", tools="hover",tooltips=tooltips)
	p.vbar(x='x', top='counts', width=0.9, source = source, line_color="white",
		fill_color=factor_cmap('x', palette=Spectral6, factors=sexs, start =1, end=2))
	p.y_range.start=0
	p.x_range.range_padding=0.1
	p.xaxis.major_label_orientation=1
	p.xgrid.grid_line_color=None		
				
	
	script, div7=components(p)
	context={'script7':script,'div7':div7}
	#context=None	
	return context
def sex_race_count(request):
	y = ecrf.objects.values('subjectid').count()
	male_ethnicity = ecrf.objects.filter(subject_sex='M').values('subject_race')
	female_ethnicity = ecrf.objects.filter(subject_sex='F').values('subject_race')
	male_eth_list = list(male_ethnicity)
	female_eth_list =list(female_ethnicity)	
	male_counter_dict = Counter(ethn['subject_race'] for ethn in male_eth_list)
	male_dict = dict(male_counter_dict)
	female_counter_dict = Counter(ethn['subject_race'] for ethn in female_eth_list)
	female_dict=dict(female_counter_dict)
	m_list_values = list(male_dict.values())
	f_list_values = list(female_dict.values())
	n_male_dict = {'male':male_dict}
	n_female_dict ={'female':female_dict}
	all_dict = {**n_male_dict,**n_female_dict}
	df = pd.DataFrame(all_dict)
	sexs = df.columns.tolist()
	races = df.index.tolist()
	ln_male_count = len(m_list_values)
	ln_female_count =len(f_list_values)
	if ln_male_count > ln_female_count:
		len_diff = ln_male_count - ln_female_count
		for i in range(len_diff):
			f_list_values.append(0)
	
	if ln_female_count > ln_male_count:
		len_diff = ln_female_count - ln_male_count
		for i in range(len_diff):
			m_list_values.append(0)
		
	data = {
		'race':races,
		'Male':m_list_values,
		'Female':f_list_values,
		}
	x = [ (r, sex) for r in races for sex in sexs]
	print(x)
	counts = sum(zip(data['Male'],data['Female']),())
	source = ColumnDataSource(data=dict(x=x,counts=counts))
	tooltips =[
		("Race, Sex","@x"),
		("Counts","@counts"),
	]
	p = figure(x_range=FactorRange(*x), plot_height=350, title="Race Counts by Sex",
			toolbar_location="right", tools="hover",tooltips=tooltips)
	p.vbar(x='x', top='counts', width=0.9, source = source, line_color="white",
		fill_color=factor_cmap('x', palette=Spectral11, factors=sexs, start =1, end=2))
	p.y_range.start=0
	p.x_range.range_padding=0.1
	p.xaxis.major_label_orientation=1
	p.xgrid.grid_line_color=None		
				
	
	script, div8=components(p)
	context={'script8':script,'div8':div8}
	#context=None	
	return context

def race_count(request):
	y = ecrf.objects.values('subjectid').count()
	eth = ecrf.objects.values('subject_race')
	eth_list=list(eth)
	ethnicity_dict = Counter(ethn['subject_race'] for ethn in eth_list)
	eth_dict=dict(ethnicity_dict)
	percent_eth = {k: round((v/y)*100) for k, v in eth_dict.items()} 
	print(percent_eth)#eth_dict={}
	#for i in eth_list:
	#	eth_dict.update(i)
	#print(eth_dict)
	
	chart_colors=['#44e5e2','#e29e44']
	pie = {
	#	'':,
	#	'':,
		}	
	color_num = len(pie)
	data = pd.Series(ethnicity_dict).reset_index(name='value').rename(columns={'index':'race'})
	data['angle'] = (data['value']/data['value'].sum()) * (2*pi)
	colours = viridis(len(eth_dict)) 
	print(colours)
	data['color'] = colours #chart_colors[:color_num]
	p = figure(
		plot_height=350,
		title="Counts of Races",
		tooltips="@race: @value",x_range=(-0.5,1.0))
	p.wedge(x=0,y=1,radius=0.4,
		start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
		line_color = "white",color='color',legend='race', source=data)

	data["value"] = data['value'].astype(str)
	data["value"] = data["value"].str.pad(35,side="left")
	print(data)
	source = ColumnDataSource(data)
	print(source)
	labels = LabelSet(x=0,y=1, text = 'value',
				angle=cumsum('angle',include_zero=True),
				source = source, render_mode='canvas')
	p.add_layout(labels)
	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color=None
	#p.line(x,y,legend='f(x)',line_width=2)
	show(p)
	script, div9=components(p)
	context={'script9':script,'div9':div9}
	return context

def race_percent(request):
	y = ecrf.objects.values('subjectid').count()
	eth = ecrf.objects.values('subject_race')
	eth_list=list(eth)
	ethnicity_dict = Counter(ethn['subject_race'] for ethn in eth_list)
	eth_dict=dict(ethnicity_dict)
	percent_eth = {k: round((v/y)*100) for k, v in eth_dict.items()} 
	print(percent_eth)#eth_dict={}
	#for i in eth_list:
	#	eth_dict.update(i)
	#print(eth_dict)
	
	chart_colors=['#44e5e2','#e29e44']
	pie = {
	#	'':,
	#	'':,
		}	
	color_num = len(pie)
	data = pd.Series(percent_eth).reset_index(name='value').rename(columns={'index':'race'})
	data['angle'] = (data['value']/data['value'].sum()) * (2*pi)
	colours = cividis(len(eth_dict)) 
	print(colours)
	data['color'] = colours #chart_colors[:color_num]
	p = figure(
		plot_height=350,
		title="Percent of Races",
		tooltips="@race: @value %",x_range=(-0.5,1.0))
	p.wedge(x=0,y=1,radius=0.4,
		start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
		line_color = "white",color='color',legend='race', source=data)

	data["value"] = data['value'].astype(str)
	data["value"] = data["value"].str.pad(35,side="left")
	print(data)
	source = ColumnDataSource(data)
	print(source)
	labels = LabelSet(x=0,y=1, text = 'value',
				angle=cumsum('angle',include_zero=True),
				source = source, render_mode='canvas')
	p.add_layout(labels)
	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color=None
	#p.line(x,y,legend='f(x)',line_width=2)
	show(p)
	script, div10=components(p)
	context={'script10':script,'div10':div10}
	return context

def age_histogram(request):
	ages=ecrf.objects.values_list('subject_age',flat=True)
	age_list=list(ages)
	print(age_list)
	age_int = [int(i) for i in age_list]
	#number of data points
	n = len(age_int)
	#using Sturges Rule for number of bins
	k = round(1 + np.log(n) ,0)
	hist,edges =np.histogram(age_int,bins=k,density=True)

def Merg_Dict(dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10):
	res ={**dict1,**dict2,**dict3,**dict4,**dict5,**dict6,**dict7,**dict8,**dict9,**dict10}
	return res

def metric_views(request):

	percent = percent_samples_in(request)
	ethn_count = ethnicity_count(request)
	ethn_percent = ethnicity_percent(request)
	sex_eth_count =sex_ethnicity_count(request)
	sex_eth_percent =sex_ethnicity_percent(request)
	sex_r_percent =sex_race_percent(request)
	sex_r_count =sex_race_count(request)
	symptom_counts = symptom_counts_cov_pos(request)
	r_count = race_count(request)
	r_percent = race_percent(request)
	age_hist =age_histogram(request)

	context = Merg_Dict(percent,ethn_count,ethn_percent,sex_eth_count,sex_eth_percent,symptom_counts,sex_r_percent,sex_r_count,r_count,r_percent) 
	#context=symptom_counts_cov_pos
	return render_to_response('rvpmetric/metrics.html',context=context)


