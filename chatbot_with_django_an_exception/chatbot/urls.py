from django.urls import path
from .views import handle_message

urlpatterns = [
    path('handle_message/<str:message>/', handle_message, name='handle_message'),
]
