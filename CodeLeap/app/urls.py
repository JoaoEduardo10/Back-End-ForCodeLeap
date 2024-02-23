from django.urls import path
from app.controllers.careersController import CareersController

urlpatterns = [
    path('', CareersController.as_view()),
]