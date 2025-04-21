from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(GenericAPIView):
    serializer_class = ProjectSerializer

    
    def get(self, request:Request):
        projects = Project.objects.all()
        serializer = self.serializer_class(instance=projects, many=True)
        response = {
            "message":"successful",
            "data":serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "data":serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)