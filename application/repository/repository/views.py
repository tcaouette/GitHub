
#from django.shortcuts import render
from django.http import HttpResponse
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

def index(request):

	context = { }
	return render(request, 'repository/repository/templates/repository/index.html', context = context)
