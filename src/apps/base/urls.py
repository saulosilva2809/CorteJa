from .views import HomeView

from django.urls import path


urlpatterns = [
    path('', view=HomeView.as_view(), name='home_view')
]
