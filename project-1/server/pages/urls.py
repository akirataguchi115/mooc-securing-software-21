from django.urls import path

from .views import homePageView
from .views import changeUsernameView

urlpatterns = [
    path('', homePageView, name='home'),
    path('change', changeUsernameView)
]
