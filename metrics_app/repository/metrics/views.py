from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy, reverse

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
from metrics.appmetrics.rvpsyndromic.rvpmetrics import gpcht_sex_race_percent
from metrics.chart import grouped_bar_chart
from metrics.make_context import create_context
#from bokeh.charts import TimeSeries

# Create your views here.

def rvp_metrics(request):
	x,counts,source,tooltips,sexs,races,male,female = gpcht_sex_race_percent()
	print(tooltips)
	script,div = grouped_bar_chart(x,counts,source,tooltips,sexs,races,male,female)
	
	context=create_context(script,div)
	#call functions to build metrics
	return render(request,'metrics/rvpmetrics.html',context=context)
