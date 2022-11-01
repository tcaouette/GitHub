
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
import csv, io
from search.models import TUpInventoryb, TUpInventorya,TListInventoryb,TListInventorya, Tblboxinfo,Aliquot_Trans,Update_Trans,Create_Aliquot_Trans,Create_Box_Trans,LoginLogout#####insert names of the class models
import operator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
import re
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from search.forms import AliquotForm, BoxForm, BoxInfoForm, AliquotUpdateForm,BoxUpdateForm,BoxContinueUpdateForm,BoxContinueCreateForm
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
#from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin, LoginRequiredMixin 
# Create your views here.
from django.contrib import messages
import pymysql
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.utils.timezone import get_current_timezone
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin


	

@login_required
def index(request):

	date_now = str(timezone.localtime(timezone.now()))

	context = {'datetime':date_now}
	return render(request, 'cdm_home/index.html', context = context)

def contacts(request):
	context ={}
	return render(request, 'cdm_home/contacts.html', context = context)
