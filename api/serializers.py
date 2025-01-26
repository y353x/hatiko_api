from rest_framework import fields, serializers

from api.constants import IMEI_LENGTH


class ImeiSerializer(serializers.Serializer):
    """Сериалайзер imei + token."""

    imei = fields.CharField(
        max_length=IMEI_LENGTH,
        min_length=IMEI_LENGTH,
        required=True,)
    token = fields.CharField(
        required=True)
