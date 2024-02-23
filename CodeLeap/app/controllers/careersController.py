from app.models import Careers
from app.database.serializers import CareersSerializer

from rest_framework.views import APIView;
from rest_framework.response import Response


class CareersController(APIView):
    def get(self, request):
        careers = Careers.objects.all()
        serializer = CareersSerializer(careers, many=True)

        return Response(serializer.data)