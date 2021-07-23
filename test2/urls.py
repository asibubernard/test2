from django.contrib import admin
from django.urls import path
from .views import country 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', country, name="country" ),
]
