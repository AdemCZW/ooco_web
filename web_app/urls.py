from django.urls import path
from .views import (
    IndexListView,
)

app_name = 'web_app'
urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
]
