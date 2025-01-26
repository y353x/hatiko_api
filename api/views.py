from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.requests import imei_check_request
from api.serializers import ImeiSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_imei(request):
    """Функция проверки imei из запроса."""

    serializer = ImeiSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        imei = int(serializer.validated_data['imei'])
        token = serializer.validated_data['token']
    except IntegrityError:
        error = 'ошибка внесения данных'
        return Response(error, status.HTTP_400_BAD_REQUEST)

    check_result = imei_check_request(imei, token)
    return Response(check_result, status.HTTP_200_OK)
