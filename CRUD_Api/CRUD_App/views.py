from django.shortcuts import render
from .models import Empmodels
from .serialize import CRUD_serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeTables(APIView):

    def get (self, request):
        empobj = Empmodels.objects.all()
        empserializerobj = CRUD_serialize(empobj, many=True)
        return Response(empserializerobj.data)

    def post(self,request):
        serializobj=CRUD_serialize(data=request.data)
        if serializobj.is_valid():
            serializobj.save()
            return Response(serializobj.data,status=status.HTTP_201_CREATED)
        return Response(serializobj.errors,status=status.HTTP_400_BAD_REQUEST)

class EmpUpdate(APIView):

    def get_object(self,pk):
        try:
            return Empmodels.objects.get(pk=pk)
        except Empmodels.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        empobj=self.get_object(pk)
        serializobj=CRUD_serialize(empobj)
        return Response(serializobj.data)

    def put(self,request,pk):
        empobj=self.get_object(pk)
        empseralizeobj=CRUD_serialize(empobj,data=request.data)
        if empseralizeobj.is_valid():
            empseralizeobj.save()
            return Response(empseralizeobj.data,status=status.HTTP_200_OK)
        return Response(empseralizeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        empobj=self.get_object(pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

