from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/', include('apps.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]
