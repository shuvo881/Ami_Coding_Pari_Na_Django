from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InputDataSerializer
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from Khoj_the_search_Page.models import InputData


@api_view(['GET'])
def get_all_input_values(request, user_id):
    print("request:", user_id)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Invalid user_id'}, status=status.HTTP_400_BAD_REQUEST)

    #start_datetime = user.start_datetime
    #end_datetime = user.end_datetime
    if True:
    #if start_datetime and end_datetime:
        input_data = InputData.objects.filter(
            user=user,
        ).order_by('timestamp')
        #timestamp__range = (start_datetime, end_datetime)
        serializer = InputDataSerializer(input_data, many=True)

        response_data = {
            'status': 'success',
            'user_id': user_id,
            'payload': serializer.data
        }
    else:
        response_data = {
            'error': 'Missing start_datetime or end_datetime for the user',
        }

    return Response(response_data)
