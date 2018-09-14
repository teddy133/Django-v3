# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.throttling import ScopedRateThrottle
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from models import Games
from models import Members
from serializers import GamesSerializer
from serializers import MembersSerializer
from models import StoreCategory
from models import Store
from models import Manager
from models import Region
from serializers import StoreCategorySerializer
from serializers import StoreSerializer
from serializers import ManagerSerializer
from serializers import ManagerRegionSerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from django.utils.translation import ugettext
from rest_framework import permissions
import custompermission



from django.shortcuts import render

# Create your views here.

class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    name = 'games-list'

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    name = 'games-detail'

class MembersList(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-list'

class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    name = 'members-detail'









class StoreCategoryList(generics.ListCreateAPIView):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
    name = 'storecategory-list'
    search_fields = ('^name',)
    ordering_fields = ('name',)



class StoreCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
    name = 'storecategory-detail'


class StoreList(generics.ListCreateAPIView):
    throttle_scope = 'stores'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    name = 'store-list'
    filter_fields = (
        'name',
        'store_category',
        'inserted_timestamp',
        'been_audited',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'been_audited',
    )





class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'stores'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    name = 'store-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
        )



class ManagerList(generics.ListCreateAPIView):
    throttle_scope = 'managers'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    name = 'manager-list'
    filter_fields = (
        'name',
        'gender',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
    'name',
    'timestamp'
    )



class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'managers'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    name = 'manager-detail'


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = ManagerRegionSerializer
    name = 'region-list'


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = ManagerRegionSerializer
    name = 'region-detail'










class GameAdministration(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
        'Games' : reverse(GamesList.name, request=request),
        'Members' : reverse(MembersList.name, request=request),
        'store-categories': reverse(StoreCategoryList.name, request=request),
        'stores': reverse(StoreList.name, request=request),
        'manager': reverse(ManagerList.name, request=request),
        'regions': reverse(RegionList.name, request=request)
        })
