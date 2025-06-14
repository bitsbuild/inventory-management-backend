from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.serializers import ItemSerializer
from restapi.models import Item
class ItemPG(APIView):
    # Creates An Item
    def post(self,request):
        try:
            serializer = ItemSerializer(data=request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # Gets All Items
    def get(self,request):
        items = Item.objects.all()
        serialized_items = ItemSerializer(data=items)
        return Response(serialized_items.data,status=status.HTTP_200_OK)
class ItemGUD(APIView):
    # Gets An Item For ID Value Specified In URL
    def get(self,request,id):
        pass
    # Updates An Item For ID Value Specified In URL
    def update(self,request,id):
        pass
    # Deletes An Item For ID Value Specified In URL
    def delete(self,request,id):
        pass
    