import requests


def generate_map(latitude, longitude, scale):
    try:
        request = requests.get('http://static-maps.yandex.ru/1.x/', params={
        'll': ','.join((latitude, longitude)),
        'spn': ','.join((scale, scale)),
        'l': 'map'
    })
        if not request:
            return False
        with open('map.png', 'wb') as writer:
            writer.write(request.content)
    except Exception:
        return False
    return True