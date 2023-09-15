from django.shortcuts import render, redirect
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from . models import advocate,company
from django.db.models import Q
from .serializers import advocateSerializer,companySerializer


@api_view(['GET',])
def endpoint(request):
    data = ['/advocate', '/advocate/:username']
    return Response(data)

#class base view

class Advocate_list(APIView):
    
    def get(self, request, format=None):
        query = request.GET.get('query')
    
        if query == None:
            query = ''
        data = advocate.objects.filter (Q(username__icontains=query) | Q(bio__icontains=query) )
        serializer = advocateSerializer(data, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = advocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" # Create your views here.

    
@api_view(['GET','POST'])
def advocate_list(request):
    #handles get request
    if request.method == 'GET':
        query = request.GET.get('query')
    
        if query == None:
            query = ''
        data = advocate.objects.filter (Q(username__icontains=query) | Q(bio__icontains=query) )
        serializer = advocateSerializer(data, many=True)
        return Response(serializer.data)
    #handle post rest
    if request.method == 'POST':
        data = advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = advocateSerializer(data, many=False)
        return Response(serializer.data)
 """
#class base views

class Advocate_details(APIView):
    def get_object(self, username):
        try:
            return advocate.objects.get(username=username)
        except advocate.DoesNotExist:
            raise Http404
        
    def get(self,request,username):
        
        data = self.get_object(username)
        serializer = advocateSerializer(data, many=False)
        return Response(serializer.data)
    
    def put(self,request,username):
        data = self.get_object(username)
        data.username = request.data['username']
        data.bio = request.data['bio']
        data.save()
        
        serializer = advocateSerializer(data, many=False)
        return Response(serializer.data)
    
    def delete(self,request,username):
        data = self.get_object(username)
        data.delete()
        return Response('susucessfull deleted')
    
    
""" 
@api_view(['GET','PUT','DELETE'])
def advocate_detail(request, username):
    #alawy get user
    data = advocate.objects.get(username=username)
    #handles get request
    if request.method == 'GET':
        serializer = advocateSerializer(data, many=False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        data.username = request.data['username']
        data.bio = request.data['bio']
        data.save()
        
        serializer = advocateSerializer(data, many=False)
        return Response(serializer.data)
        
        
    #handle put request
    if request.method == "DELETE":
        data.delete()
        return Response('susucessfull deleted')
 """
@api_view(['GET'])
def company_list(request):
    list = company.objects.all()
    serializer = companySerializer(list, many=True)
    return Response(serializer.data)
 