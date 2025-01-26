import re

from rest_framework import fields, serializers, status
from rest_framework.exceptions import ValidationError

from api.constants import IMEI_LENGTH, IMEI_REGEX


class ImeiSerializer(serializers.Serializer):
    """Сериалайзер imei + token."""

    imei = fields.CharField(
        max_length=IMEI_LENGTH,
        min_length=IMEI_LENGTH,
        required=True,)
    token = fields.CharField(
        required=True)

    def validate_imei(self, value):
        if not re.match(IMEI_REGEX, str(value)):
            raise ValidationError(
                detail='Wrong imei. Should contain 15 digits only',
                code=status.HTTP_400_BAD_REQUEST)
        return value
