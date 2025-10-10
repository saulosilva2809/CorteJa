from .views import HomeView, ServicesView

from django.urls import path


urlpatterns = [
    path('', view=HomeView.as_view(), name='home_view'),
    path('services/', view=ServicesView.as_view(), name='services_view'),
]
