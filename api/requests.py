import requests


def imei_check_request(imei, service_token):
    """Проверка imei на imeicheck."""

    url = 'https://api.imeicheck.net/v1/checks'
    data = {'deviceId': imei,
            'serviceId': 1}
    headers = {'Authorization': f'Bearer {service_token}'}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 201:
        return response.json().get('properties')
    return response.json().get('message')
