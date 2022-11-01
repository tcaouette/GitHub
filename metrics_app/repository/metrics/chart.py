from metrics.appmetrics.rvpsyndromic.rvpmetrics import gpcht_sex_race_percent
from collections import Counter
import re
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
import datetime
from datetime import timedelta
from collections import Counter
from django_pandas.io import read_frame
import pandas as pd
from math import pi
from bokeh.palettes import Spectral11,Spectral6,colorblind,Inferno, BuGn, brewer, Category20c,magma,d3, Category10, Dark2, viridis, all_palettes, cividis




def grouped_bar_chart(x,data,source,tooltips,sexs,races,male,female):
	

	p = figure(x_range=FactorRange(*x), plot_height=350, title="Race Percentage by Sex",
			toolbar_location="right", tools="hover",tooltips=tooltips)
	p.vbar(x='x', top='counts', width=0.9, source = source, line_color="white",
		fill_color=factor_cmap('x', palette=Spectral6, factors=sexs, start =1, end=2))
	p.y_range.start=0
	p.x_range.range_padding=0.1
	p.xaxis.major_label_orientation=1
	p.xgrid.grid_line_color=None		
				
	
	script, div=components(p)
	#context={'script':script,'div':div}
	return script, div


