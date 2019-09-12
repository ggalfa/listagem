from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listagem/', views.list_events),
    path('', RedirectView.as_view(url='/listagem/')),
]
