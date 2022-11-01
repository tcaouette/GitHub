from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.urls import reverse_lazy, reverse
#from rvpsyndromic.forms import Stg0_flu1, Stg0_flu2, TStg0Brpcr, TStg0Ecrf
#from rvpsyndromic.models import TStg0Brpcr, TStg0Ecrf, TStg0Refcov2Pcr1, TStg0Refcov2Pcr2, TStg0Refflupcr1, TStg0Refflupcr2, TStg1Brpcr, TStg1Cov2Pcr, TStg1Ecrf, TStg1Refflupcr
import re
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
	return render(request, 'rdt/index.html', context = context)
