from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Count,Sum
import csv, io
from search.models import TUpCoa, SearchCreateLocationTrans,TUpSearch,TUpSearchTest, TUpInventoryb, TUpInventorya,TListInventoryb,TListInventorya, Tblboxinfo,Aliquot_Trans,Update_Trans,Create_Aliquot_Trans,Create_Box_Trans,LoginLogout,SearchFreezeThawTrans,SearchReturnTrans,SearchShippingTrans,TRefSite###insert names of the class models
import operator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
import re
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from search.forms import LocationForm,  AliquotForm, BoxForm, BoxInfoForm, AliquotUpdateForm,BoxUpdateForm,BoxContinueUpdateForm,BoxContinueCreateForm
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
import tzlocal 
from django_tables2 import tables, TemplateColumn, SingleTableView
from search.tables import TUpSearchTable
from search.filters import TUpSearchFilter
from django_filters.views import FilterView
from dal import autocomplete
#from haystack.query import SearchQuerySet
#from haystack.generic_views import SearchView

def login(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user =  auth.authenicate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request,user)
		return HttpResponseRedirect("/account/login/")

def logout(request):
	auth.logout(request)


#@background(exp_time=60*1051200)# two year hold time
#def two_year_hold(aqid):

	
@login_required
def index(request):

	num_freezer =TUpInventoryb.objects.all().count()
	num_aliquots = TUpInventorya.objects.all().count()	

	context = {'num_freezer': num_freezer,'num_aliquots':num_aliquots}
	return render(request, 'search/index.html', context = context)

@login_required
def help_me(request):

	context = {}
	return render(request, 'search/help.html', context = context)



@user_passes_test(lambda u:u.is_superuser)
def csv_upload(request):
	date_now = str(timezone.now())
	
	if request.method=="GET":
		return render(request,'search/csv_upload.html')

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)

	for column in csv.reader(io_string, delimiter=',',quotechar='|'):
		#boxid_obj, created = TUpInventoryb.objects.update_or_create(
		#boxid=column[4],
		#freezer=column[0],
		#cage=column[1],
		#cane=column[2],
		#stack=column[3],
		
		#invnum=0,
		#insertdate=date_now,
		#invcomments=column[5]
		#)
		_, created= TUpSearchTest.objects.get_or_create(

		lotid=column[1],
		trialkey=column[2],
		studyid=column[3],
		studydesc=column[4],
		aqid=column[5],
		originalid=column[6],
		grid=column[7],
		labelinfo=column[8],
		volume=column[9],
		insertdate=date_now,
		invnum=0,
		invcomment=column[10],
		boxid=column[0],
		checkout=0,
		age=column[11],
		gender=column[12],
		demogroup=column[13],
		riskcategory=column[14],
		riskgroupdesc=column[15],
		bloodtype=column[16],
		hiv1=column[17],
		hiv2=column[18],
		hivo=column[19],
		hbs=column[20],
		hbc=column[21],
		hav=column[22],
		hcv=column[23],
		mmrv=column[24],
		influenza=column[25],
		sars_cov2=column[26],
		other=column[27],
		manufacturer=column[28],
		panelname=column[29],
		paneldesc=column[30],
		membernum=column[31],
		samtypedesc=column[32],
		samprepdesc=column[33],
		notes=column[34],
		dup=column[35],
		isconfirmed=column[36]
		)
	context ={}	
	return render(request, 'search/csv_upload.html',context=context)

def normalize_query(query_string,
	findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
	normspace=re.compile(r'\s{2,}').sub):

	return[normspace(' ',t[0] or t[1].strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):

	query = None
	terms = normalize_query(query_string)

	for term in terms:
		or_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query

class SamTypeDesc(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs =TUpSearch.object.all()
		if self.q:
			qs = qs.filter(samtypedesc__istartswith==self.q)
		return self.q	

class big_table(FilterView,LoginRequiredMixin, StaffuserRequiredMixin):
	#model = TUpSearch
	#context_object_name = 'aliquots'
	filterset_class = TUpSearchFilter
	template_name = 'search/big_table.html'

	#def get(self, *args, **kwargs):
	#	if 'd' in self.request.GET:
	#		response = HttpResponse(content_type='text/css')
	#		response['Content-Disposition']='attachment; filename="aliquot.csv"'
	#		writer = csv.writer(response, delimiter=',')
	#		writer.writerow(['aqid','boxid','cage','cane','stack','originalid','grid','labelinfo','volume','insertdate'])

	#		for i in found_entries:
	#			writer.writerow([i.aqid,i.boxid,i.boxid.cage,i.boxid.cane,i.boxid.stack, i.originalid, i.grid,i.labelinfo,i.volume,i.insertdate])
	#		return response

def search_aliquot(request):
	aliquots = TUpSearch.objects.all()
	bool(aliquots)
	aliquot = aliquots
	#aqid = [aqid.aliquots  for aqid in aliquots]
	#samtypedesc = [samtypedesc.aliquots for samtypedesc in aliquots]
	#gender = [gender.aliquots for gender in aliquots]	
	context={'aliquot':aliquot}
	return render(request, 'search/aliquot_search.html', context=context)		
	 


	
	
@login_required
def aliquot_table(request):
	query_string = ''
#	paginator=None
#	page =None
	num_found = str(TUpSearch.objects.exclude(checkout=1)[:10].count())
	num_all = str(TUpSearch.objects.exclude(checkout=1).count())
	user = request.user.get_username()
	date_now = str(timezone.now())
#	found_entries = TUpInventorya.objects.exclude(checked_out=1)[:10]
	found_entries = TUpSearch.objects.exclude(checkout=1).order_by('aqid')
	page = request.GET.get('page',1)
	paginator=Paginator(found_entries,500)
	try:
		found_entries = paginator.page(page)
	except PageNotAnInteger:
		found_entries = paginator.page(1)
	except EmptyPage:
		found_entries = paginator.page(paginator.num_pages)
#	num_found = str(TUpInventorya.objects.exclude(checked_out=1).count())
#	num_all = num_found
	if request.method=='POST':
	
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TUpSearch.objects.filter(aqid__in=list_of_id)
		list_of_obj.update(checkout=1)
		list_of_obj.update(user=user)
		list_of_obj.update(date_changed = date_now)

		found_entries = TUpSearch.objects.exclude(checkout=1).order_by('aqid')
		page = request.GET.get('page',1)
		paginator=Paginator(found_entries,500)
		try:
			found_entries = paginator.page(page)
		except PageNotAnInteger:
			found_entries = paginator.page(1)
		except EmptyPage:
			found_entries = paginator.page(paginator.num_pages)
				 
	if 'all' in request.GET:
		found_entries = TUpSearch.objects.exclude(checkout=1)
		page = request.GET.get('page',1)
		paginator=Paginator(found_entries, 100)
		try:
			found_entries = paginator.page(page)
		except PageNotAnInteger:
			found_entries = paginator.page(1)
		except EmptyPage:
			found_entries = paginator.page(paginator.num_pages)
		num_found = str(TUpSearch.objects.exclude(checkout=1).count())
		num_all = num_found

	if('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['boxid__boxid','boxid__cage','boxid__cane','boxid__stack','boxid__freezer','aqid','originalid','grid','labelinfo','volume'])
		found_entries = TUpSearch.objects.filter(entry_query).exclude(checkout=1)
		num_found = str(found_entries.count())
		num_all = str(TUpSearch.objects.exclude(checkout=1).count())

	if 'd' in request.GET:
		response = HttpResponse(content_type='text/css')
		response['Content-Disposition']='attachment; filename="aliquot.csv"'
		writer = csv.writer(response, delimiter=',')
		writer.writerow(['aqid','boxid','cage','cane','stack','originalid','grid','labelinfo','volume','insertdate'])

		for i in found_entries:
			writer.writerow([i.aqid,i.boxid,i.boxid.cage,i.boxid.cane,i.boxid.stack, i.originalid, i.grid,i.labelinfo,i.volume,i.insertdate])
		return response
	else:
		context = {'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page}
	return render(request, 'search/aliquots_table.html', context=context)		



def locations(request):
	location = TRefSite.objects.all().order_by('siteid')
	context ={'location':location}
	return render(request, 'search/all_locations.html',context=context)	


@login_required
def meta_table(request):
	query_string = ''
	num_found =str(Tblboxinfo.objects.all()[:10].count())
	num_all =str(Tblboxinfo.objects.all().count())

	found_entries =Tblboxinfo.objects.all().order_by('boxid') 
	page = request.GET.get('page',1)
	paginator=Paginator(found_entries,50)
	try:
		found_entries = paginator.page(page)
	except PageNotAnInteger:
		found_entries = paginator.page(1)
	except EmptyPage:
		found_entries = paginator.page(paginator.num_pages)
	if 'all' in request.GET:
		found_entries = Tblboxinfo.objects.all()
		num_found = str(Tblboxinfo.objects.all().count())
		num_all = num_found

	if('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['boxid__boxid','contents','boxtype','insertdate','invstatus','boxid__freezer'])
		found_entries = Tblboxinfo.objects.filter(entry_query)
		
		num_found = str(found_entries.count())
		num_all = str(Tblboxinfo.objects.all().count())

	if 'd' in request.GET:
		response = HttpResponse(content_type='text/css')
		response['Content-Disposition']='attachment; filename="metacontents.csv"'
		writer = csv.writer(response, delimiter=',')
		writer.writerow(['boxtype','boxid','contents','insertdate','invstatus'])

		for i in found_entries:
	
			writer.writerow([i.boxtype,i.boxid.boxid,i.contents,i.insertdate, i.invstatus ])

		return response
	else:
		context = {'query_string':query_string, 'found_entries':found_entries, 'num_found':num_found, 'num_all':num_all,'page':page}
	return render(request, 'search/meta_table.html', context=context)		

@user_passes_test(lambda u:u.is_superuser)
def coa(request):
	coa=TUpCoa.objects.all()[:5]
	context={'coa':coa}
	return render(request, 'search/coa.html',context=context)

@login_required
def AliquotList2(request, pk):
	user = request.user.get_username()
	date_now = str(timezone.now())
	aliquot = TUpSearch.objects.filter(boxid=pk).order_by('aqid')
	thaw_count = SearchFreezeThawTrans.objects.all().values('aqid').order_by('aqid').annotate(total_thaw=Count('datetime_thaw'))
	if request.method=='POST':
		reason = 'Checked out Aliquot'	
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TUpSearch.objects.filter(aqid__in=list_of_id)
		list_of_obj.update(checkout=1)
		list_of_obj.update(user=user)
		list_of_obj.update(date_changed = date_now)
		messages.success(request, "Aliquots {} Checked Out Successfully!".format(list_of_id))
		aliquot = TUpSearch.objects.filter(boxid=pk)
		thaw = 1

		for i in list_of_id:
			list_update = Update_Trans.objects.create(aqid=i, boxid=pk, updated=1, date_updated=date_now, user=user, reason=reason)
		for a in list_of_id:
			tup_aqid = TUpSearch.objects.get(aqid=a)
			print(tup_aqid)	
			list_freeze_thaw = SearchFreezeThawTrans.objects.update_or_create(aqid = tup_aqid, freeze_thaw=thaw, datetime_thaw=date_now, user=user)

	#	freeze_count =list(SearchFreezeThawTrans.objects.all().values('aqid').order_by('aqid').annotate(t_total=Count('datetime_thaw')))
	#	for f in freeze_count:
	#		TUpSearch.objects.filter(aqid=f['aqid']).update(freeze_thaw = f['t_total'])		
			
	context={'aliquot':aliquot}
	return render(request,'search/aliquot_detail.html',context=context)

def AliquotShipping(request, pk):
	user = request.user.get_username()
	date_now = str(timezone.now())
	locations = TRefSite.objects.all()
	print(locations)
	aliquot = TUpSearch.objects.filter(boxid=pk).order_by('aqid')
	if request.method=='POST':
		reason='Shipping of Aliquot'
		location = request.POST.get('location')
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TUpSearch.objects.filter(aqid__in=list_of_id)
		list_of_obj.update(checkout = 2)
		list_of_obj.update(user=user)
		list_of_obj.update(date_changed = date_now)
		list_of_obj.update(ship_location=location)
		print(location)
		messages.success(request, "Aliquots {} Shipped Successfully!".format(list_of_id))
		aliquot = TUpSearch.objects.filter(boxid=pk)
		for i in list_of_obj:
			list_update = SearchShippingTrans.objects.create(aqid_out=i, boxid_out=pk, ship_location=location, date_shipped=date_now, user=user, condition='Frozen')
	
	context={'aliquot':aliquot,'locations':locations}
	return render(request,'search/shipping.html',context=context)

def AliquotShippingReturn(request):
	user = request.user.get_username()
	date_now = str(timezone.now())
	box = TUpInventoryb.objects.all() 
	locations = TRefSite.objects.all()
	location=""
	if request.method=='POST' and 'ship_location' in request.POST:
		 
		location = request.POST.get('location')
		print(location)
	aliquot = TUpSearch.objects.filter(ship_location=location).order_by('aqid')
		#shipping = SearchShippingTrans.objects.filter('aqid_out'=i).order_by('aqid_out')	
	boxid_out =[]
	condition =[]
	volume =[]
	date_return =[]
	shipped_location =[]
	freeze_thaw =[]
	user_list=[]
	shipping=[]
	if request.method=='POST' and 'update' in request.POST:
		reason='Return of Aliquot'
		#volume = request.POST.getlist('volume')
		list_of_id = request.POST.getlist('for_action')
		for i in list_of_id:
			volume.append(request.POST.get('v_'+i))
			date_return.append(request.POST.get('d_'+i))
			boxid_out.append(request.POST.get('b_'+i))
			condition.append(request.POST.get('c_'+i))
			shipped_location.append(request.POST.get('s_'+i))
			freeze_thaw.append(request.POST.get('f_'+i))
			user_list.append(user)	
		tup_results =[ {'aqid':ids,'volume':vol,'boxid':box_out,'freeze_thaw':ft} for ids, vol, d_return, box_out, cond,ft in zip(list_of_id,volume,date_return, boxid_out, condition,freeze_thaw)]
		print(tup_results)
		return_results =[ {'aqid_in':ids,'date_returned':d_return,'boxid_in':box_out,'condition':cond,'user':u} for ids,  d_return, box_out, cond,u in zip(list_of_id,date_return, boxid_out, condition,user_list)]
		print(return_results)
		update_shipping =[{'aqid_out':ids,'date_returned':d_return,'boxid_in':b_in} for d_return, b_in, ids in zip(date_return, boxid_out,list_of_id)]

		return_results =[ {'aqid_in':ids,'ship_location':s_loc,'date_returned':d_return,'boxid_in':box_out,'condition':cond,'user':u} for  ids, s_loc, d_return, box_out, cond,u in zip(list_of_id,shipped_location,date_return, boxid_out, condition,user_list)]
		for i in list_of_id:
			for k in tup_results:
				if k['aqid']==i:
					TUpSearch.objects.filter(aqid=i).update(**k)
		

		for j in return_results:
			SearchReturnTrans.objects.create(**j)
	
		list_of_obj = TUpSearch.objects.filter(aqid__in=list_of_id)
		list_of_obj.update(checkout = -2)
		list_of_obj.update(user=user)
		list_of_obj.update(date_changed = date_now)
		messages.success(request, "Aliquots {} Returned Successfully!".format(list_of_id))
		#aliquot = TUpSearch.objects.filter(checkout=2).order_by('aqid')
	#	for i in list_of_id:
	#		returns = SearchShippingTrans.objects.filter('aqid_out'=i).order_by('aqid_out')	
			
		#for i in list_of_id:
		#	for k in update_shipping:
		#		if k['aqid_out']== i:	
		#			list_update = SearchShippingTrans.objects.filter(aqid_out=i).update(**k)
	
	context={'aliquot':aliquot, 'locations':locations,'box':box}
	return render(request,'search/shipping_return.html',context=context)

def BoxGrid(request, pk):
	user = request.user.get_username()
	date_now = str(timezone.now())
	aliquot = TUpSearch.objects.filter(boxid=pk).order_by('aqid')
	position_list= TUpSearch.objects.filter(boxid=pk).values_list('grid',flat=True)
	box_size =Tblboxinfo.objects.filter(boxid=pk).values('boxtype')
	
	position_id_10 = []

	pos_list=[]
	for position in position_list:
		if position != None:
			pos_list.append(position)
	print(pos_list)	

	x =0
	
	for size in box_size:
		if size['boxtype'] =='10x10':
			x = 10
			position_id_10 = ['A01','A02','A03','A04','A05','A06','A07','A08','A09','A10','B01','B02','B03','B04','B05','B06','B07','B08','B09','B10',
			'C01','C02','C03','C04','C05','C06','C07','C08','C09','C10','D01','D02','D03','D04','D05','D06','D07','D08','D09','D10',
			'E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','F01','F02','F03','F04','F05','F06','F07','F08','F09','F10',
			'G01','G02','G03','G04','G05','G06','G07','G08','G09','G10','H01','H02','H03','H04','H05','H06','H07','H08','H09','H10',
			'I01','I02','I03','I04','I05','I06','I07','I08','I09','I10','J01','J02','J03','J04','J05','J06','J07','J08','J09','J10'] 
			
		elif size['boxtyp']=='9x9':
			x = 9
		
		else:
			x='No-Size'
	print(x)
			
	
	thaw_count = SearchFreezeThawTrans.objects.all().values('aqid').order_by('aqid').annotate(total_thaw=Count('datetime_thaw'))
	if request.method=='POST':
		reason = 'Checked out Aliquot'	
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TUpSearch.objects.filter(aqid__in=list_of_id)
		list_of_obj.update(checkout=1)
		list_of_obj.update(user=user)
		list_of_obj.update(date_changed = date_now)
		messages.success(request, "Aliquots {} Checked Out Successfully!".format(list_of_id))
		aliquot = TUpSearch.objects.filter(boxid=pk)
		thaw = 1

		for i in list_of_id:
			list_update = Update_Trans.objects.create(aqid=i, boxid=pk, updated=1, date_updated=date_now, user=user, reason=reason)
		for a in list_of_id:
			tup_aqid = TUpSearch.objects.get(aqid=a)
			print(tup_aqid)	
			list_freeze_thaw = SearchFreezeThawTrans.objects.update_or_create(aqid = tup_aqid, freeze_thaw=thaw, datetime_thaw=date_now, user=user)

		freeze_count =list(SearchFreezeThawTrans.objects.all().values('aqid').order_by('aqid').annotate(t_total=Count('datetime_thaw')))
		for f in freeze_count:
			TUpSearch.objects.filter(aqid=f['aqid']).update(freeze_thaw = f['t_total'])		
			
	context={'aliquot':aliquot,'x':x,'pos_list':pos_list,'pos_10_id':position_id_10 }
	return render(request,'search/box_grid.html',context=context)

@login_required
def AliquotDispose(request, pk):
	user = request.user.get_username()
	date_now = str(timezone.now())
	aliquot = TUpSearch.objects.filter(boxid=pk).order_by('aqid')
	
	if request.method=='POST':
		reason='Disposed of Aliquot'
		list_of_id = request.POST.getlist('for_action')
		list_of_obj = TUpSearch.objects.filter(aqid__in=list_of_id)
		list_of_obj.update(checkout = -1)
		list_of_obj.update(user=user)
		list_of_obj.update(date_changed = date_now)
		messages.success(request, "Aliquots {} Disposed Successfully!".format(list_of_id))
		aliquot = TUpSearch.objects.filter(boxid=pk)
		for i in list_of_id:
			list_update = Update_Trans.objects.create(aqid=i, boxid=pk, updated=-1, date_updated=date_now, user=user, reason=reason)
	
	context={'aliquot':aliquot}
	return render(request,'search/aliquot_dispose.html',context=context)

@login_required
def AliquotFreezeThaw(request):
	user = request.user.get_username()
	date_now = str(timezone.now())
	#aliquot = SearchFreezeThawTrans.objects.all()
	aliquot = TUpSearchTest.objects.filter(boxid='001A')
	
	context={'aliquot':aliquot}
	return render(request,'search/aliquot_fztw.html',context=context)

@login_required
def FreezerList(request):
	user = request.user.get_username()
	date_now = str(timezone.now())
	freezer_filter = TUpInventoryb.objects.all().values('freezer').distinct()
	cage_filter = TUpInventoryb.objects.all().values('cage').distinct()
	cane_filter = TUpInventoryb.objects.all().values('cane').distinct()
	stack_filter = TUpInventoryb.objects.all().values('stack').distinct()
	found_entries = TUpInventoryb.objects.all().order_by('boxid')
	 
	page = request.GET.get('page',1)
	paginator=Paginator(found_entries,50)
	try:
		found_entries = paginator.page(page)
	except PageNotAnInteger:
		found_entries = paginator.page(1)
	except EmptyPage:
		found_entries = paginator.page(paginator.num_pages)

	if('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['boxid','cage','cane','stack','freezer','invnum','insertdate','invcomments'])
		found_entries = TUpInventoryb.objects.filter(entry_query)
		
	
	context={'freezer':found_entries, 'freezer_filter':freezer_filter, 'cage_filter':cage_filter, 'cane_filter':cane_filter,'stack_filter':stack_filter,'page':page}
	return render(request,'search/freezer.html',context=context)

class LocationCreate(SuccessMessageMixin,LoginRequiredMixin,StaffuserRequiredMixin,CreateView):
	model=TRefSite
	form_class=LocationForm 
	template_name = 'search/add_location.html'
	success_url = reverse_lazy('search:meta_table')
#	def get_success_url(self):
	#	aqid = self.kwargs['pk']
#		boxid = self.#kwargs['pk'][:4]
		#aqid = self.form.cleanded_data['aqid']	
#		return reverse('search:aliquot_add_multi',kwargs={'pk':self.object.aqid})#self.object.aqid})#str(aqid)})#self.object.boxid.boxid})
	def form_valid(self, form):
		date_now=str(timezone.now())
		instance = form.save(commit=False)
		location = form.cleaned_data['sitename']
		location_abbr = form.cleaned_data['siteabbr']
		instance.user = self.request.user.get_username()
		insert_data = SearchCreateLocationTrans(location=location,locatino_abbr=location_abbr, date_created=date_now,user=instance.user)
		insert_data.save()
	
		return super(LocationCreate,self).form_valid(form)
	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "Location {} Added!".format(cleaned_data['siteabbr'])
	
class AliquotCreate(SuccessMessageMixin,LoginRequiredMixin,StaffuserRequiredMixin,CreateView):
	model=TUpSearch
	form_class=AliquotForm 
	template_name = 'search/aliquot_add.html'
	#success_url = reverse_lazy('search:aliquot_add')
	def get_success_url(self):
	#	aqid = self.kwargs['pk']
#		boxid = self.#kwargs['pk'][:4]
		#aqid = self.form.cleanded_data['aqid']	
		return reverse('search:aliquot_add_multi',kwargs={'pk':self.object.aqid})#self.object.aqid})#str(aqid)})#self.object.boxid.boxid})
	def form_valid(self, form):
		date_now=str(timezone.now())
		instance = form.save(commit=False)
		aqid = form.cleaned_data['aqid']
		instance.user = self.request.user.get_username()
		insert_data = Create_Aliquot_Trans(aqid=aqid, date_created=date_now,user=instance.user)
		insert_data.save()
	
		return super(AliquotCreate,self).form_valid(form)
	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "Aliquot {} Added!".format(cleaned_data['aqid'])
class AliquotCreateMulti(SuccessMessageMixin,LoginRequiredMixin,StaffuserRequiredMixin,CreateView):
	model=TUpSearch
	form_class=AliquotForm 
	template_name = 'search/aliquot_add.html'
	#success_url = reverse_lazy('search:aliquot_add'
	def get_initial(self):
		aqid = self.kwargs['pk']
		print(aqid)
		initial_values = TUpSearch.objects.filter(aqid=aqid).values('originalid','checkout','lotid','trialkey','studyid','studydesc','grid','insertdate','invnum','volume','age','gender','demogroup','riskcategory','riskgroupdesc','bloodtype','hiv1','hiv2','hivo','hbs','hbc','hav','hcv','mmrv','influenza','sars_cov2','other','manufacturer','panelname','paneldesc','membernum','samtypedesc','samprepdesc','dup','isconfirmed','invcomment','labelinfo','notes')
		for i in initial_values:	
			print(i)	
		initial=super(AliquotCreateMulti,self).get_initial()
		initial['aqid']=aqid
		initial['originalid']=i['originalid']
		initial['checkout']=i['checkout']
		initial['lotid']=i['lotid']
		initial['trialkey']=i['trialkey']
		initial['studyid']=i['studyid']
		initial['studydesc']=i['studydesc']
		initial['grid']=i['grid']
		initial['insertdate']=i['insertdate']
		initial['invnum']=i['invnum']
		initial['volume']=i['volume']
		initial['age']=i['age']
		initial['gender']=i['gender']
		initial['demogroup']=i['demogroup']
		initial['riskcategory']=i['riskcategory']
		initial['riskgroupdesc']=i['riskgroupdesc']
		initial['bloodtype']=i['bloodtype']
		initial['hiv1']=i['hiv1']
		initial['hiv2']=i['hiv2']
		initial['hivo']=i['hivo']
		initial['hbs']=i['hbs']
		initial['hbc']=i['hbc']
		initial['hav']=i['hav']
		initial['hcv']=i['hcv']
		initial['mmrv']=i['mmrv']
		initial['influenza']=i['influenza']
		initial['sars_cov2']=i['sars_cov2']
		initial['other']=i['other']
		initial['manufacturer']=i['manufacturer']
		initial['panelname']=i['panelname']
		initial['paneldesc']=i['paneldesc']
		initial['membernum']=i['membernum']
		initial['samtypedesc']=i['samtypedesc']
		initial['samprepdesc']=i['samprepdesc']
		initial['dup']=i['dup']
		initial['isconfirmed']=i['isconfirmed']
		initial['invcomment']=i['invcomment']
		initial['labelinfo']=i['labelinfo']
		initial['notes']=i['notes']
		return initial
			
	def get_success_url(self):
	#	aqid = self.kwargs['pk']
#		boxid = self.#kwargs['pk'][:4]
		#aqid = self.form.cleanded_data['aqid']	
		return reverse('search:aliquot_add_multi',kwargs={'pk':self.object.aqid})#self.object.aqid})#str(aqid)})#self.object.boxid.boxid})
	def form_valid(self, form):
		date_now=str(timezone.now())
		instance = form.save(commit=False)
		aqid = form.cleaned_data['aqid']
	
		instance.user = self.request.user.get_username()
		insert_data = Create_Aliquot_Trans(aqid=aqid, date_created=date_now,user=instance.user)
		insert_data.save()
		
		return super(AliquotCreateMulti,self).form_valid(form)
	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "Aliquot {} Added!".format(cleaned_data['aqid'])



class AliquotDelete(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
	model = TUpInventorya
	template_name = 'search/aliquot_delete.html'
	success_url = reverse_lazy('search:aliquot_table')
	context_object_name = 'aliquot'
	def form_valid(self, form):
		return super().form_valid(form)

	 
class AliquotUpdate(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
	model = TUpSearch 
	form_class = AliquotUpdateForm
	template_name ='search/aliquot_update.html'
	
	def get_success_url(self):
	#	aqid = self.kwargs['pk']
#		boxid = self.#kwargs['pk'][:4]
		#aqid = self.form.cleanded_data['aqid']	
		return reverse('search:aliquot_detail',kwargs={'pk':self.object.boxid.boxid})#self.object.aqid})#str(aqid)})#self.object.boxid.boxid})
#		return reverse('aliquot_detail',kwargs={'pk':boxid} )		
	def get_success_message(self,cleaned_data):
		#print(cleaned_data)
		return " Aliquot {} Updated!".format(cleaned_data['aqid'])
	
	def form_valid(self, form):
		date_now=str(timezone.now())

		instance = form.save(commit=False)
		instance.aqid = self.kwargs['pk']
		aqid = TUpSearch.objects.get(aqid=instance.aqid)
		#print(aqid)
		instance.user = self.request.user.get_username()
		reason = form.cleaned_data['reason']
		boxid = form.cleaned_data['boxid']
		checkout = form.cleaned_data['checkout']
		insert_data = Update_Trans(updated=1,aqid=instance.aqid, date_updated=date_now,user=instance.user,reason=reason,boxid=boxid)
		#insert_data.save()
		print(instance.checkout)
		old = list(TUpSearch.objects.filter(aqid = instance.aqid).values('checkout'))
		print(old)
		for o in old:
			print(o['checkout'])
		if instance.checkout != o['checkout']:
			if checkout == 1:
				print('checkout is one')
				thaw = 1
				freeze_thaw_instance = SearchFreezeThawTrans(aqid=aqid,freeze_thaw=thaw, datetime_thaw=date_now,user=instance.user)
				freeze_thaw_instance.save()
				#instance.freeze_thaw = instance.freeze_thaw + 1
	
			if checkout == 0:
				print('checkout is zero')
				freeze=0  
				freeze_thaw_instance = SearchFreezeThawTrans(aqid=aqid,freeze_thaw=freeze, datetime_freeze=date_now,user=instance.user)
				freeze_thaw_instance.save()
				#instance.freeze_thaw = instance.freeze_thaw + 1
					

		insert_data.save()
		
		return super(AliquotUpdate,self).form_valid(form)
					

class BoxCreate(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	model = TUpInventoryb
	form_class=BoxForm 
	template_name = 'search/box_add.html'
	
	success_url = reverse_lazy('search:box_add_continue')

	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "First part of box {} created successfully! Continue filling out the form.".format(cleaned_data['boxid'])


	def form_valid(self, form):
		date_now=str(timezone.now())
		instance = form.save(commit=False)
		boxid = form.cleaned_data['boxid']
		instance.user = self.request.user.get_username()
		insert_data = Create_Box_Trans(boxid=boxid, date_created=date_now,user=instance.user)
		insert_data.save()

		return super().form_valid(form)

	


class BoxDelete(LoginRequiredMixin, StaffuserRequiredMixin, DeleteView):
	model = TUpInventoryb
	template_name = 'search/box_delete.html'
	success_url = reverse_lazy('search:box')
	context_object_name = 'box'

	 
class BoxUpdate(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
	model = TUpInventoryb
	form_class = BoxUpdateForm
	template_name ='search/box_update.html'

	def get_success_url(self):

		return reverse('search:box_continue',kwargs={'pk':self.object.boxid})
		
	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "First part of box {} updated successfully! Continue filling out the form.".format(cleaned_data['boxid'])

	def form_valid(self, form):
		date_now=str(timezone.now())

		instance = form.save(commit=False)
		instance.boxid = self.kwargs['pk']
		instance.user = self.request.user.get_username()
		reason = form.cleaned_data['reason']
			
		insert_data = Update_Trans(updated=1,boxid=instance.boxid, date_updated=date_now,user=instance.user,reason=reason)
		insert_data.save()
		
		return super(BoxUpdate,self).form_valid(form)
		

class BoxDetail(DetailView):
	model = TUpInventoryb

class BoxContinueUpdate(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
	model=Tblboxinfo
	form_class=BoxContinueUpdateForm
	template_name='search/box_continue.html'
	success_url = reverse_lazy('search:meta_table')
					
	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "Box {} Updated Successfully!".format(cleaned_data['boxid'])
	

class BoxContinueCreate(SuccessMessageMixin,LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
	model=Tblboxinfo
	form_class=BoxContinueCreateForm
	template_name='search/box_add_continue.html'
	success_url = reverse_lazy('search:meta_table')

	def get_success_message(self,cleaned_data):
		print(cleaned_data)
		return "Second part of box {} created successfully!.".format(cleaned_data['boxid'])

@login_required
def freezer_B(request):
	search_term =None
	num_freezer =TUpInventoryb.objects.all().count()
	freezer = TUpInventoryb.objects.all()
	
	
	if 'search' in request.GET:
		search_term = request.GET['search']
		freezer = freezer.filter(freezer__icontains=search_term)
		

	context = {'num_freezer': num_freezer,'search_term':search_term,'freezer':freezer }
	return render(request, 'search/search_freezer_b.html', context = context)

def freezer_A(request):
	freezer = TUpInventoryb.objects.all()
	
	context = {'num_freezer': num_freezer,'search_term':search_term,'freezer':freezer }
	return render(request, 'search/search_freezer_a.html', context = context)



@login_required
def aliquot(request):
	search_term = ''
	aliquot = None
	box = None

	if('search' in request.GET) and request.GET['search'].strip():
		query_string = request.GET['search']
		aliquot_query = get_query(query_string, ['boxid__boxid','boxid__cage','boxid__cane','boxid__stack','boxid__freezer','aqid','originalid','grid','labelinfo','volume'])
		box_query = get_query(query_string, ['boxid__boxid'])
		aliquot = TUpInventorya.objects.filter(aliquot_query).order_by('-volume')
		box = Tblboxinfo.objects.filter(box_query)	
	

	context = {'aliquot':aliquot,'box':box}
	return render( request, 'search/aliquots.html', context = context)
				 
@login_required
def box(request):

	search_term = ''
	boxinfo = None
	box = None
	if 'search' in request.GET:
		search_term=request.GET['search']
		box = TUpInventoryb.objects.filter(boxid__icontains=search_term).select_related()
		boxinfo = Tblboxinfo.objects.filter(boxid__boxid__icontains=search_term).select_related()
		


	context = {'boxinfo':boxinfo,'box':box}
	return render( request, 'search/box.html', context = context)

class ContentsDetailView(generic.ListView):
	model = TListInventoryb
	template_name = 'search/contents.html'
	context_object_name = 'content_details'

