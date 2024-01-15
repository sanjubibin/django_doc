from django.urls import path
from .views import HomePageView, AboutPageView, SaveDataFromFilesToDataBase

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('read_csv_and_and_update_db/', SaveDataFromFilesToDataBase.as_view(), name="read_csv_and_and_update_db_page")
]
