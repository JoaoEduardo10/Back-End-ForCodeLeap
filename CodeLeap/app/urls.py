from django.urls import path

from app.controllers.careersController import CareersController

urlpatterns = [
    path('', CareersController.as_view(), name="create_and_get_careers"),
    path('<int:id>/', CareersController.as_view(), name="update_delete_careers"),
]