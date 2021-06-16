from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    # My views
    path('profile/', views.Profile.as_view(), name='profile'),
]
