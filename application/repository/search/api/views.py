from django.db.models import Q
from rest_framework import generics, mixins

from search.models import TUpInventoryb, TUpInventorya
from .permissions import IsOwnerOrReadOnly
from .serializers import TUPBSerializer, TUPASerializer


class TUPBapiView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field ='boxid'
	serializer_class = TUPBSerializer

	def get_queryset(self):
		qs=TUpInventoryb.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(freezer__icontains=query)|Q(cage__icontains=query))
		return qs

	def perform_create(self, serializer):
		serializer.save()
	def post(self, request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class TUPBrudView(generics.RetrieveUpdateDestroyAPIView):
	
	lookup_field ='boxid'
	serializer_class = TUPBSerializer

	def get_queryset(self):
		return TUpInventoryb.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}


class TUPAapiView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field ='aqid'
	serializer_class = TUPASerializer

	def get_queryset(self):
		qs=TUpInventorya.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(aqid__icontains=query)|Q(labelinfo__icontains=query))
		return qs

	def perform_create(self, serializer):
		serializer.save()

	def post(self, request, *args, **kwargs):
		return self.create(request,*args,**kwargs)

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}

class TUPArudView(generics.RetrieveUpdateDestroyAPIView):
	
	lookup_field ='aqid'
	serializer_class = TUPASerializer

	def get_queryset(self):
		return TUpInventorya.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {"request":self.request}
