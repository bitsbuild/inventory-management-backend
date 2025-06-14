from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restapi.serializers import ItemSerializer
from restapi.models import Item
from drf_yasg.utils import swagger_auto_schema
class ItemPG(APIView):
    # Creates An Item
    @swagger_auto_schema(request_body=ItemSerializer)
    def post(self,request):
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # Gets All Items
    def get(self,request):
        items = Item.objects.all()
        serialized_items = ItemSerializer(items,many=True)
        return Response(serialized_items.data,status=status.HTTP_200_OK)
class ItemGUD(APIView):
    # Gets An Item For ID Value Specified In URL
    def get(self,request,id):
        try:
            item = Item.objects.get(pk=id)
            ser_item = ItemSerializer(item)
            return Response(ser_item.data,status=status.HTTP_200_OK)
        except:
            return Response(ser_item.errors,status=status.HTTP_404_NOT_FOUND)
    # Updates An Item For ID Value Specified In URL
    @swagger_auto_schema(request_body=ItemSerializer)
    def put(self,request,id):
        item = Item.objects.get(pk=id)
        serializer = ItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # Deletes An Item For ID Value Specified In URL
    def delete(self,request,id):
        try:
            Item.objects.get(pk=id).delete()
            return Response({"status":"specified object deleted"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"deletion process failed","error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    