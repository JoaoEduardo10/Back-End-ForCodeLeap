from app.models import Careers
from app.database.serializers import CareersSerializer

from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class CareersController(APIView):

    def get_object(self, id):
        try:
            return Careers.objects.get(pk=id)
        except Careers.DoesNotExist:
            raise NotFound



    def get(self, _request):
        careers = Careers.objects.all()
        serializer = CareersSerializer(careers, many=True)

        return Response(serializer.data)
    
    def post(self, request):


        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'username': request.data.get('username',)
        }

        serializer = CareersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def patch(self, request, id):
        careers = self.get_object(id)

        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'username': request.data.get('username', careers.username),
            'created_datetime': request.data.get('id', careers.created_datetime)
        }

        serializer = CareersSerializer(careers, data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
    
        return Response(serializer.errors, status=404)
    
    def delete(self, _request, id):
        try:
            careers = self.get_object(id)
            careers.delete()
            return Response({}, status=200)
        except Exception:
            return Response("Unable to delete.",status=404)
