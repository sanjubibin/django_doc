from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet

# Create your views here.

class SnippetApiView(APIView):
    def post(self, request):
        data = self.request.data

        serialized_data = SnippetSerializer(data = data)
        if serialized_data.is_valid():
            dt = serialized_data.save()
            response_data = {
                "status": "create success",
                "created_obj": f"Snippet object({dt.pk})" if dt else "no objects created"
            }
        else:
            response_data = {
                "status": "Failure",
            }

        return Response(response_data)
    
    def put(self, request):
        data = self.request.data

        id_to_update = data["id"]
        data_to_update = data["data_to_update"]
    
        object_to_update = Snippet.objects.get(pk = id_to_update)

        serialized_data = SnippetSerializer(object_to_update, data = data_to_update)
        if serialized_data.is_valid():
            dt = serialized_data.save()
            response_data = {
                "status": "update success",
                "created_obj": f"Snippet object({dt.pk}) has update" if dt else "no objects created"
            }
        else:
            response_data = {
                "status": "Failure",
            }

        return Response(response_data)