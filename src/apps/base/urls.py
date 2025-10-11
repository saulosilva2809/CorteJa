from .views import (
    HomeView,
    ProfessionalsView,
    ServicesView
)

from django.urls import path


urlpatterns = [
    path('', view=HomeView.as_view(), name='home_view'),
    path('professionals/', view=ProfessionalsView.as_view(), name='professionals_view'),
    path('services/', view=ServicesView.as_view(), name='services_view'),
]
