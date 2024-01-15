from django.shortcuts import render

from django.views.generic import TemplateView, View
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas
import csv
# Create your views here.

from app1.models import LocationUSADataModel
from app1.serializer import LocationUSADataModelSerializer


class HomePageView(TemplateView):
    template_name = 'app1/homepage.html'

class AboutPageView(TemplateView):
    template_name = 'app1/aboutpage.html'


class SaveDataFromFilesToDataBase(APIView):
    def get(self, request):
        read_data_of_csv = pandas.read_csv("app1/csv_files/copy_exported.csv")
        print("state with max population",read_data_of_csv["population"].max())

        created_instance=[]
        with open("app1/csv_files/copy_exported.csv", "r") as csv_file:
            # print("type11111111111:::::::", type(csv_file))
            file = csv.DictReader(csv_file) #NOTE: 
            for index, row in enumerate(file):
                # print("index:::::::", index)
                # print("row:::::::::", row)
                save_to_db = LocationUSADataModelSerializer(data = row)
                if save_to_db.is_valid():
                    # save_to_db.save()
                    created_instance.append(dict(row))
        
        data = {
            "dtt": created_instance
        }
        return Response(data)
        
class OtherThings(APIView):
    def get(self, request):

        
        pass