from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        if user.groups.filter(name="Manager").exists():
            return Response({"is_manager": True, "message": "User is in the Manager group"})
        return Response({"is_manager": False, "message": "User is not in the Manager group"})