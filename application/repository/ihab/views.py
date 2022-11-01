from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import csv, io
from ihab.models import stg1_dataentryperson_ihab_abid_1, stg1_dataentryperson_ihab_abid_2#####insert names of the class models
import operator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
import re
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from ihab.forms import DE_Form_ihab_abid_1, DE_Form_ihab_abid_2,BCW_Primary, BCW_Secondary,BLD_Primary,BLD_Secondary
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
#from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin, LoginRequiredMixin 
# Create your views here.
from django.contrib import messages
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
import numpy as np
import datetime
from datetime import timedelta
from collections import Counter
from django_pandas.io import read_frame
import pandas as pd
from math import pi
from bokeh.palettes import Spectral11,colorblind,Inferno, BuGn, brewer
from ihab.ABID_PDF_to_Excel import *

def index(request):
	context = { }
	if request.method =='POST':
		print(os.getcwd())
		main()
		print('hello')
	return render(request, 'ihab/index.html', context = context)
def contacts(request):
	context ={}
	return render(request, 'ihab/contacts.html', context = context)

def metric(request):
	y = stg1_dataentryperson_ihab_abid_1.objects.values('site_code','date_insert')
	y2 = stg1_dataentryperson_ihab_abid_2.objects.values('site_code','date_insert')
	k = list(y.values('date_insert'))
	k2 =list(y2.values('date_insert'))
	df1 = read_frame(y)
	df2 = read_frame(y2)
		
	df1['date_insert']= pd.to_datetime(df1['date_insert'])
	df2['date_insert']= pd.to_datetime(df2['date_insert'])
	df1['data_entry'] ='primary' 
	df2['data_entry'] = 'secondary'
	frames = [df1,df2]
	df3 = pd.concat(frames)
	#df3['Week/Year'] = df3['date_insert'].apply(lambda x:"%d/%d" % (x.week, x.year))
	#df3 = df3.groupby(['Week/Year','site_code'])
	wide = df3.pivot_table(index='date_insert', columns='data_entry', aggfunc=len,fill_value=0).reset_index()
	wide.columns = wide.columns.droplevel(0)	
	wide.columns = ['date_insert', 'primary', 'secondary']
	wide['date'] = wide.date_insert.apply(lambda x: x.date)
	wide['month'] = wide.date_insert.apply(lambda x: x.month)
	wide['day'] = wide.date_insert.apply(lambda x: x.day)
	#print(wide)	
	temp_df = wide.groupby(['date']).sum().reset_index()	
	cats = ['primary', 'secondary']	
	temp_df.drop(['day'], axis=1, inplace =True)
	temp_df.drop(['month'], axis=1, inplace =True)
	#temp_df.drop(['data_entry'], axis=1,inplace=True)
	#temp_df.reset_index(inplace= True)	
	
	print(temp_df)
	TOOLS ="save, pan, box_zoom, reset, wheel_zoom, tap"
	source = ColumnDataSource(temp_df)
	p = figure(x_axis_type='datetime',plot_width=1000, title="Data Entry Type wise count of data entry by day", toolbar_location='above',tools=TOOLS)

	colors=brewer['Dark2'][3]

	p.vbar_stack(cats, x='date',width=timedelta(days=0.5), color=['orange','blue'], source = source, legend=[value(x) for x in cats])

	p.y_range.start=0
	p.x_range.range_padding =0.1
	p.xgrid.grid_line_color =None
	p.axis.minor_tick_line_color =None
	p.xaxis.axis_label ='Date'
	p.xaxis.formatter=DatetimeTickFormatter(
#		date=["%d %B %Y"],
		days=["%d %B %Y"],
		months=["%d %B %Y"],
		years=["%d %B %Y"],
		)
	p.xaxis[0].ticker =DaysTicker(days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])		
	p.xaxis.major_label_orientation =pi/4
	p.yaxis.axis_label ='total number of data entries'
	p.legend.location ="top_left"
	p.legend.orientation = "horizontal"
	p.add_tools(HoverTool(
	tooltips =[('date','@date{%F}'),('total count','$y'),('primary count','@primary'),('secondary count','@secondary')], formatters={'@date':'datetime'},
		 ))

		
	script, div=components(p)
	context={'script':script,'div':div}
	#print(temp_df.head())
	return render_to_response('ihab/metric.html',context=context)

def pdf_to_sql(request):
	if request.method =='POST':
		# import function to run
		#from ihab.ABID_PDF_to_Excel import main
		# call function
		main()
		print('hello')	
	return HttpResponseRedirect(reverse('ihab:index_home'))
	



class BLD_Primary_Create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	model = stg1_dataentryperson_ihab_abid_1
	form_class = BLD_Primary
	template_name = 'ihab/bld_primary_add.html'


	def get_success_url(self):
		return reverse('ihab:index_home')

	def get_success_message(self,cleaned_data):
		return "Form Submitted Successfully! Site Code Submitted: {}".format(cleaned_data['site_code'])

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.user = self.request.user.get_username()
		self.object.date_insert = date_now
		self.object.save()
		return super().form_valid(form)
	

class BLD_Secondary_Create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	model = stg1_dataentryperson_ihab_abid_2#
	form_class = BLD_Secondary
	template_name = 'ihab/bld_secondary_add.html'

	def get_success_url(self):
		return reverse('ihab:index_home')
	def get_success_message(self,cleaned_data):
		return "Form Submitted Successfully! Site Code Submitted: {}".format(cleaned_data['site_code'])
		
	

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.user = self.request.user.get_username()
		self.object.date_insert = date_now
		self.object.save()
		return super().form_valid(form)


class BCW_Primary_Create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	model = stg1_dataentryperson_ihab_abid_1
	form_class = BCW_Primary
	template_name = 'ihab/bcw_primary_add.html'

	def get_success_url(self):
		return reverse('ihab:index_home')
	def get_success_message(self,cleaned_data):
		return "Form Submitted Successfully! Site Code Submitted: {}".format(cleaned_data['site_code'])
		
	
	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.user = self.request.user.get_username()
		self.object.date_insert = date_now
		self.object.save()
		return super().form_valid(form)
	
class BCW_Secondary_Create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	model = stg1_dataentryperson_ihab_abid_2#
	form_class = BCW_Secondary
	template_name = 'ihab/bcw_secondary_add.html'
	def get_success_url(self):
		return reverse('ihab:index_home')
	def get_success_message(self,cleaned_data):
		return "Form Submitted Successfully! Site Code Submitted: {}".format(cleaned_data['site_code'])
	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.user = self.request.user.get_username()
		self.object.date_insert = date_now
		self.object.save()
		return super().form_valid(form)
	
