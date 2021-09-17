from django.urls import path, include

urlpatterns = [
    path('image/', include('apps.image.urls')),
]
