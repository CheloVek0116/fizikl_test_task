from django.urls import path

from apps.image.views import FlipImageView

urlpatterns = [
    path('flip/', FlipImageView.as_view()),
]
