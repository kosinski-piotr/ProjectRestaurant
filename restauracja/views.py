from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Danie,RodzajDan, Klient, Zamowienie
from .serializers import RodzajDanSerializer, DanieSerializer, ZamowienieSerializer, KlientSerializer, UserSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User




class RodzajDanList(generics.ListCreateAPIView):
    queryset = RodzajDan.objects.all()
    serializer_class = RodzajDanSerializer
    name = 'rodzajdan-list'
    filterset_fields = ['nazwa']
    search_fields = ['nazwa']
    ordering_fields = ['nazwa']


class RodzajDanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RodzajDan.objects.all()
    serializer_class = RodzajDanSerializer
    name = 'rodzajdan-detail'



class DaniaList(generics.ListCreateAPIView):
    queryset = Danie.objects.all()
    serializer_class = DanieSerializer
    name = 'danie-list'
    filter_fields = ['nazwa', 'rodzajDania', 'dataDodaniaDania', 'przepis', 'czasPrzygotowania','cena','User']
    search_fields = ['nazwa', 'czasPrzygotowania']
    ordering_fields = ['nazwa', 'rodzajDania', 'czasPrzygotowania']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DaniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Danie.objects.all()
    serializer_class = DanieSerializer
    name = 'danie-detail'
   # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class KlientFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='dataUrodzenia', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='dataUrodzenia', lookup_expr='lte')

    class Meta:
        model = Klient
        fields = ['from_birthdate','to_birthdate']

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    filter_class = KlientFilter
    name = 'klient-list'
    ordering_fields = ['nazwisko', 'dataUrodzenia']


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'

class ZamowienieFilter(FilterSet):
    min_cena = NumberFilter(field_name='cena', lookup_expr='gte')
    max_cena = NumberFilter(field_name='cena', lookup_expr='lte')
    klient_nazwisko = AllValuesFilter(field_name='klient__nazwisko')

    class Meta:
        model = Zamowienie
        fields = ['min_cena', 'max_cena', 'klient_nazwisko']


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    filter_class = ZamowienieFilter
    name = 'zamowienie-list'


class ZamowienieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-detail'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'RodzajDan': reverse(RodzajDanList.name, request=request),
                         'Dania': reverse(DaniaList.name, request=request),
                         'Klienci': reverse(KlientList.name, request=request),
                         'Zamowienia': reverse(ZamowienieList.name, request=request),
                         'Userzy': reverse(UserList.name, request=request)
})





    
