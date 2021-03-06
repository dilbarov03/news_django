from django.urls import path, include # new
from django.views.generic.base import TemplateView # new
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('articles/', include('articles.urls')), # new
    path('', include('pages.urls')),
]
