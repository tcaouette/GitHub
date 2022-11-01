
from metrics.appmetrics.rvpsyndromic.rvpmetrics import gpcht_sex_race_percent
from metrics.chart import grouped_bar_chart


def create_context(script, div):

	context={'script':script,'div':div}

	return context


def merge_context(context):
	#merge context dictionaries
	return context
