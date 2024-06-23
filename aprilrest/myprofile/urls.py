from django.urls import path
from .views import Take,takeprofile
urlpatterns = [
    path('apiview/<str:key>',Take.as_view()),
    path('apipost',takeprofile.as_view())
]
