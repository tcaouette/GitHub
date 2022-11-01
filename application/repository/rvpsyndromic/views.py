from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy, reverse
from rvpsyndromic.forms import Stg0_flu1, Stg0_flu2, TStg0Brpcr, TStg0Ecrf,Stg1_Flu_Update,Stg1_Brpcr_Update,Stg1_Ecrf_Update,Stg1_Cov2_Update
from rvpsyndromic.models import TStg0Brpcr, TStg0Ecrf, TStg0Refcov2Pcr1, TStg0Refcov2Pcr2, TStg0Refflupcr1, TStg0Refflupcr2, TStg1Brpcr, TStg1Cov2, TStg1Ecrf, EcrfExclusionTrans,BrpcrExclusionTrans,Stg1Cov2PcrExclTrans,Stg1RefflupcrExclTrans,TStg1FlupcrUpdate,TStg1ReffluMismatch,TStg1ReffluMatch,TStg1BrpcrUpdate,TStg1EcrfUpdate,TStg1Cov2Update,TStg1Refflu,TStg1ReffluInvalid,TStg1BrpcrInvalid,TStg1Cov2Invalid

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
import numpy as np
import datetime
from datetime import timedelta
from collections import Counter
from django_pandas.io import read_frame
import pandas as pd
from math import pi
from bokeh.palettes import Spectral11,colorblind,Inferno, BuGn, brewer

# Create your views here.
def index(request):
	context = { }
	#messages.success(request, "Entered into DB ")
	return render(request, 'rvpsyndromic/index.html', context = context)

def dataentry_page(request):
	context = { }
	#messages.success(request, "Entered into DB ")
	return render(request, 'rvpsyndromic/dataentry_page.html', context = context)
def metrics_page(request):
	context = { }
	#messages.success(request, "Entered into DB ")
	return render(request, 'rvpsyndromic/metrics_page.html', context = context)
def recon_page(request):
	context = { }
	#messages.success(request, "Entered into DB ")
	return render(request, 'rvpsyndromic/recon_page.html', context = context)

def updates_page(request):
	context = { }
	#messages.success(request, "Entered into DB ")
	return render(request, 'rvpsyndromic/updates_page.html', context = context)

def views_page(request):
	context = { }
	#messages.success(request, "Entered into DB ")
	return render(request, 'rvpsyndromic/views_page.html', context = context)

class stg1_flu_create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	#model = TStg0Refflupcr1
	form_class = Stg1_Flu_Update 
	template_name = 'rvpsyndromic/stg1_flu_create.html'
	#success_message = 'Primary Data Entry Person Data added!'
	#success_url = reverse_lazy('rvpsyndromic:index_rvp')
	def get_success_url(self):
		return reverse('rvpsyndromic:index_rvp')
	def get_success_message(self,cleaned_data):
		print("GET THE MESSAGE!")
		return " InfA/InfB/RSV Reference Data {} Updated!".format(cleaned_data['sample'])


	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.userid = self.request.user.get_username()
		print(self.object.userid)
		self.object.post_date = date_now
		if self.object.userid == 'bmathison':
			self.object.dep = 1
		if self.object.userid =='PVakharia':
			self.object.dep = 2

	#	self.object.save()
		return super().form_valid(form)

class stg1_brpcr_create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	#model = TStg0Refflupcr1
	form_class = Stg1_Brpcr_Update 
	template_name = 'rvpsyndromic/stg1_brpcr_create.html'
	#success_message = 'Primary Data Entry Person Data added!'
	#success_url = reverse_lazy('rvpsyndromic:index_rvp')
	def get_success_url(self):
		return reverse('rvpsyndromic:index_rvp')
	def get_success_message(self,cleaned_data):
		print("GET THE MESSAGE!")
		return " BRPCR Data For Sample {} Updated!".format(cleaned_data['sampleid'])

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.userid = self.request.user.get_username()
		print(self.object.userid)
		self.object.post_date = date_now

#		self.object.save()
		return super().form_valid(form)

class stg1_ecrf_create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	#model = TStg0Refflupcr1
	form_class = Stg1_Ecrf_Update 
	template_name = 'rvpsyndromic/stg1_ecrf_create.html'
	#success_message = 'Primary Data Entry Person Data added!'
	#success_url = reverse_lazy('rvpsyndromic:index_rvp')
	def get_success_url(self):
		return reverse('rvpsyndromic:index_rvp')
	def get_success_message(self,cleaned_data):
		print("GET THE MESSAGE!")
		return " ECRF Data For Sample {} Updated!".format(cleaned_data['subjectid'])

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.userid = self.request.user.get_username()
		print(self.object.userid)
		self.object.post_date = date_now

	#	self.object.save()
		return super().form_valid(form)

class stg1_cov2_create(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	#model = TStg0Refflupcr1
	form_class = Stg1_Cov2_Update 
	template_name = 'rvpsyndromic/stg1_cov2_create.html'
	#success_message = 'Primary Data Entry Person Data added!'
	#success_url = reverse_lazy('rvpsyndromic:index_rvp')
	def get_success_url(self):
		return reverse('rvpsyndromic:index_rvp')
	def get_success_message(self,cleaned_data):
		print("GET THE MESSAGE!")
		return " SARS-CoV-2 Data For Sample {} Updated!".format(cleaned_data['sampleid'])

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.userid = self.request.user.get_username()
		print(self.object.userid)
		self.object.post_date = date_now

#		self.object.save()
		return super().form_valid(form)


class stg0_flu1_create(SuccessMessageMixin,CreateView, LoginRequiredMixin, StaffuserRequiredMixin):
	#model = TStg0Refflupcr1
	form_class = Stg0_flu1 
	template_name = 'rvpsyndromic/stg0_flu1.html'
	#success_message = 'Primary Data Entry Person Data added!'
	#success_url = reverse_lazy('rvpsyndromic:index_rvp')
	def get_success_url(self):
		return reverse('rvpsyndromic:index_rvp')
	def get_success_message(self,cleaned_data):
		print("GET THE MESSAGE!")
		return " InfA/InfB/RSV Data For Sample {} Created!".format(cleaned_data['sample'])

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.ref1_entered_by = self.request.user.get_username()
		self.object.ref1_entereddate = date_now
		self.object.save()
		return super().form_valid(form)



class stg0_flu2_create(SuccessMessageMixin,CreateView, LoginRequiredMixin, StaffuserRequiredMixin):
	#model = TStg0Refflupcr2
	form_class = Stg0_flu2 
	template_name = 'rvpsyndromic/stg0_flu2.html'
	#success_message = 'Primary Data Entry Person Data added!'
	#success_url = reverse_lazy('index')
	def get_success_url(self):
		return reverse('rvpsyndromic:index_rvp')
	def get_success_message(self,cleaned_data):
		print("GET THE MESSAGE!")
		return " InfA/InfB/RSV Data For Sample {} Created!".format(cleaned_data['sample'])

	def form_valid(self, form):
		date_now = str(timezone.localtime(timezone.now()))
		self.object = form.save(commit=False)
		self.object.ref2_entered_by = self.request.user.get_username()
		self.object.ref2_entereddate = date_now
		self.object.save()
		return super().form_valid(form)

@login_required
def stg0_flu1_table(request):
	found_entries =TStg0Refflupcr1.objects.all()#.order_by('boxid') 
	context = {'found_entries':found_entries}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}
	return render(request, 'rvpsyndromic/stg0_flu1_table.html', context=context)


def stg1_match(request):
	match = TStg1ReffluMatch.objects.all()
	fields = [f.name for f in TStg1ReffluMatch._meta.get_fields()]
	print(fields)
	context={'match':match,'fields':fields}
	return render(request,'rvpsyndromic/stg1_match.html',context=context)

def stg1_mismatch(request):
	mismatch = TStg1ReffluMismatch.objects.all()
	fields = [f.name for f in TStg1ReffluMismatch._meta.get_fields()]
	print(fields)
	context={'match':mismatch,'fields':fields}
	return render(request,'rvpsyndromic/stg1_mismatch.html',context=context)

@login_required
def stg1_brpcr(request):	
	brpcr = TStg1Brpcr.objects.all()
	
	context = {'brpcr':brpcr}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}
	return render(request, 'rvpsyndromic/stg1_brpcr.html', context=context)	

@login_required
def stg1_ecrf_view(request):	
	ecrf = TStg1Ecrf.objects.all()
	print(ecrf)
	
	context = {'ecrf':ecrf}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}
	return render(request, 'rvpsyndromic/stg1_ecrf_view.html', context=context)

@login_required
def stg1_cov2pcr(request):	
	cov2pcr = TStg1Cov2.objects.all()
	context = {'cov2pcr':cov2pcr}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}
	return render(request, 'rvpsyndromic/stg1_cov2pcr.html', context=context)	


def stg1_refflu(request):
	refflu = TStg1Refflu.objects.all()
	context={'refflu':refflu}
	return render(request,'rvpsyndromic/stg1_refflu.html',context=context)

def stg1_refflu_inv(request):
	reffluinv = TStg1ReffluInvalid.objects.all()
	context={'reffluinv':reffluinv}
	return render(request,'rvpsyndromic/stg1_refflu_inv.html',context=context)

def stg1_brpcr_inv(request):
	brpcrinv = TStg1BrpcrInvalid.objects.all()
	context={'brpcrinv':brpcrinv}
	return render(request,'rvpsyndromic/stg1_brpcr_inv.html',context=context)

def stg1_cov2_inv(request):
	cov2inv = TStg1Cov2Invalid.objects.all()
	context={'cov2inv':cov2inv}
	return render(request,'rvpsyndromic/stg1_cov2_inv.html',context=context)




def stg1_refflupcr(request):	
	user = request.user.get_username()
	date_now = str(timezone.now())
	refflupcr = TStg1Refflupcr.objects.all().order_by('refflupcrrow_1')
	
	if request.method=='POST':
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TStg1Refflupcr.objects.filter(refflupcrrow_1__in=list_of_id)
		list_of_obj.update(refflupcrexcld = 1)
		flu = TStg1Refflupcr.objects.filter(refflupcrrow_1__in=list_of_id).values_list('refflupcrrow_1','refflupcrrow_2','refrun_date')
		#messages.success(request, "Aliquots {} Disposed Successfully!".format(list_of_id))
		for f in flu:
			list_update = Stg1RefflupcrExclTrans.objects.create(refflupcrrow_1=f[0],refflupcrrow_2=f[1],refrun_date=f[2], user=user, date_exclusion=date_now)
	context = {'refflupcr':refflupcr}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}
	return render(request, 'rvpsyndromic/stg1_refflupcr.html', context=context)	
#@login_required
def stg0_ecrf_table(request):
	query_string = ''

	ecrf =TStg0Ecrf.objects.all()#.order_by('boxid') 
	if request.method=='POST':
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TStg0Ecrf.objects.filter(subjectid__in=list_of_id)
		list_of_obj.update(sampleexclud = 1)
		specimenid = TStg0Ecrf.objects.filter(subjectid__in=list_of_id).values_list('subjectid','specimenid','ecrfrow')
		#messages.success(request, "Aliquots {} Disposed Successfully!".format(list_of_id))
		for s in specimenid:
			list_update = EcrfExclusionTrans.objects.create(subjectid=s[0],specimenid=s[1],ecrfrow=s[2], user=user, date_exclusion=date_now)
	context = {'ecrf':ecrf}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}

	context = {'found_entries':found_entries}#'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page#}
	return render(request, 'rvpsyndromic/stg0_ecrf_table.html', context=context)		


