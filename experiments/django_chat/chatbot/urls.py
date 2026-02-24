from django.urls import path

from .views import handle_message, history

urlpatterns = [
    path("chat/", handle_message, name="handle_message"),
    path("history/", history, name="history"),
]
