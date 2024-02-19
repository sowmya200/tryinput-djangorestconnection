

from .models import UserInput
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInputSerializer

class UserInputView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserInputSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            user_input = serializer.validated_data['user_input']
            return Response({'detail': f'Success! Received user input: {user_input}'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        # Your GET request logic here
        return Response({'detail': 'GET request handled successfully'}, status=status.HTTP_200_OK)    
