from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import FileResponse
from .serializers import FileSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.settings import api_settings
from rest_framework_csv import renderers
import csv
import json
import ast
from collections import defaultdict

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8-sig').splitlines()
        reader = csv.DictReader(decoded_file)
        if file_serializer.is_valid():
            file_serializer.save()
            output=[]
            for line in reader:
                mydic=defaultdict(dict)
                for key,value in line.items():
                        mydic[key]=int(value) if value.isdigit() else value
                output.append(mydic)
            return Response(output,status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
