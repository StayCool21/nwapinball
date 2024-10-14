from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # URL for the privacy policy
    path('privacy-policy/', TemplateView.as_view(template_name='home/privacyPolicy.html'), name='privacy_policy'),
]
