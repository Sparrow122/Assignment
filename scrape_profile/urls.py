from django.urls import path
from .views import Scrape_View

urlpatterns = [
    path('profile/', Scrape_View.as_view(), name='profdata')
]