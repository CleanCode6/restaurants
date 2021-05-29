import googlemaps
import urllib.request
import requests
from PIL import Image
from io import BytesIO


class MapGenerator:
    def __init__(self):
        self.largura = 640
        self.alturaplus = 640
        self.final = Image.new("RGB", (self.largura, self.alturaplus))
        self.key = "AIzaSyDkYz98ZtXHh6qcv7rhWAANiUK6-Qbdj9A"

    def request_map_url(self, params):
        # loc은 x,y 좌표를 하나의 string으로 
        urlparams = urllib.parse.urlencode({'center': params,
                                            'zoom': '17',
                                            'size': '%dx%d' % (self.largura, self.alturaplus),
                                            'maptype': 'roadmap',
                                            'markers': 'color:blue|label:S|' + params,
                                            'key': self.key})
        url = 'https://maps.googleapis.com/maps/api/staticmap?' + urlparams
        return url