from django.urls import path

from app.controllers.careersController import CareersController

urlpatterns = [
    path('', CareersController.as_view()),
    path('<int:id>/', CareersController.as_view()),
]