from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.common.models import Country,Region
from apps.common.serializer import CountrySerializer,RegionSerializer

class CountryListView(GenericAPIView):
 
    def get_queryset(self):
        country=Country.objects.all()
        return country

    def get(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=CountrySerializer(queryset,many=True)
        return Response({"countries":serializer.data},status=status.HTTP_200_OK)

        
    
class RegionListView(GenericAPIView):

    def get_queryset(self):
        regions=Region.objects.all()
        return regions
    def get(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=RegionSerializer(queryset,many=True)

        return Response({"regions":serializer.data})


