# yourappname/urls.py

from django.urls import path
from .views import UserInputView

urlpatterns = [
    path('user-input/', UserInputView.as_view(), name='user-input'),
    # Add more paths for your app's views as needed
]
