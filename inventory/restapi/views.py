from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.serializers import ItemSerializer
from restapi.models import Item
class ItemCR(APIView):
    def post(self,request):
        try:
            serializer = ItemSerializer(data=request.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        items = Item.objects.all()
        serialized_items = ItemSerializer(data=items)
        return Response(serialized_items.data,status=status.HTTP_200_OK)
