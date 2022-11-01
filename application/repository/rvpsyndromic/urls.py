from django.urls import path
from . import views
from . import metrics
app_name='rvpsyndromic'

urlpatterns = [

	path('rvp_home', views.index, name='index_rvp'),
	path('metrics/', views.metrics_page, name='metrics'),
	path('percent_samples_in/', metrics.percent_samples_in, name='percent_in'),
	path('metrics_dashboard/', metrics.metric_views, name='dashboard'),
	path('dataentry/', views.dataentry_page, name='dataentry'),
	path('reconciliation/', views.recon_page, name='recon'),
	path('views/', views.views_page, name='views'),
	path('updates/', views.updates_page, name='updates'),
	path('stg1_ecrf_view/', views.stg1_ecrf_view, name='stg1_ecrf_view'),
	path('stg1_match/', views.stg1_match, name='stg1_match'),
	path('stg1_mismatch/', views.stg1_mismatch, name='stg1_mismatch'),
	path('stg1_brpcr/', views.stg1_brpcr, name='stg1_brpcr'),
	path('stg1_brpcr_excluded/', views.stg1_brpcr_inv, name='brpcrinv'),
	path('stg1_cov2pcr/', views.stg1_cov2pcr, name='stg1_cov2pcr'),
	path('stg1_cov2_excluded/', views.stg1_cov2_inv, name='cov2inv'),
	path('stg1_refflupcr/', views.stg1_refflupcr, name='stg1_refflupcr'),
	path('stg1_refflu/', views.stg1_refflu, name='refflu'),
	path('stg1_refflu_excluded/', views.stg1_refflu_inv, name='reffluinv'),
	path('stg0_flu1/', views.stg0_flu1_create.as_view(), name='stg0_flu1'),
	path('stg0_flu2/', views.stg0_flu2_create.as_view(), name='stg0_flu2'),
	path('stg1_flu_update/', views.stg1_flu_create.as_view(), name='stg1_flu_create'),
	path('stg1_brpcr_update/', views.stg1_brpcr_create.as_view(), name='stg1_brpcr_create'),
	path('stg1_ecrf_update/', views.stg1_ecrf_create.as_view(), name='stg1_ecrf_create'),
	path('stg1_cov2_update/', views.stg1_cov2_create.as_view(), name='stg1_cov2_create'),

]
