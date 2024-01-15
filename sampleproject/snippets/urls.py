from django.urls import path
from snippets.views import SnippetApiView


urlpatterns = [
    path('', SnippetApiView.as_view(), name= "snippet_api_view")
]
