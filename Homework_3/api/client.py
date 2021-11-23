import json
import requests

from urllib.parse import urljoin
from utils import constants as const
from utils import locations


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.base_url = const.URL
        self.email = const.EMAIL
        self.password = const.PASSWORD

        self.session = requests.Session()
        self.mc = None
        self.sdc = None
        self.csrf = None

    def headers(self, location):
        return {
            'Referer': urljoin(self.base_url, location),
            'X-CSRFToken': self.csrf
        }

    def segment_structure(self, segment_name):
        return {
            "name": segment_name,
            "logicType": "or",
            "pass_condition": 1,
            "relations": [{
                "object_type": "remarketing_player",
                "params": {
                    "left": 365,
                    "right": 0,
                    "type": "positive"
                }
            }]
        }

    def campaign_structure(self, campaign_name, image_id, url_id):
        return {
            'name': campaign_name,
            'objective': 'traffic',
            'package_id': '961',
            'price': '3.2',
            'banners': [{
                'content': {
                    'image_240x400': {
                        'id': image_id
                    }
                },
                'name': '',
                'textblocks': {},
                'urls': {
                    'primary': {
                        'id': url_id
                    }
                }
            }]

        }

    def _request(self, method, location, headers=None, data=None, params=None, files=None, allow_redirects = False,
                 expected_status=200, join_url = True, jsonify=False):
        if (join_url):
            url = urljoin(self.base_url, location)
        else:
            url = location

        response = self.session.request(method, url, headers=headers, data=data, params=params, files=files,
                                        allow_redirects=allow_redirects)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')

        if jsonify:
            json_response = response.json()
            return json_response

        return response

    def post_login(self):
        headers = {
            'Referer': self.base_url
        }
        data = {
            'email': self.email,
            'password': self.password,
            'continue': urljoin(self.base_url, locations.CONTINUE_LOCATION),
            'failure': const.FAILURE_LOGIN_URL
        }

        response = self._request('POST', locations.LOGIN_LOCATION, headers=headers, data=data, allow_redirects=True,
                                 join_url=False)

        self.get_csrftoken()

        return response

    def get_csrftoken(self):
        headers = {
            'Referer': urljoin(self.base_url, 'dashboard')
        }

        response = self._request('GET', locations.CSRF, headers=headers, allow_redirects=True)

        self.csrf = response.cookies.get('csrftoken')

    def post_create_segment(self, segment_name):
        data = json.dumps(self.segment_structure(segment_name))

        response = self._request('POST', locations.CREATE_SEGMENT,
                                 headers=self.headers(locations.REFERER_CREATE_SEGMENT), data=data, jsonify=True)
        return response.get('id')

    def delete_delete_segment(self, segment_id):
        response = self._request('DELETE', locations.DELETE_SEGMENT.format(segment_id),
                                 headers=self.headers(locations.REFERER_DELETE_SEGMENT), expected_status=204)
        return response

    def get_segment(self, segment_id, expected_status):
        response = self._request('GET', locations.GET_SEGMENT.format(segment_id),
                                 headers=self.headers(locations.REFERER_GET_SEGMENT.format(segment_id)),
                                 expected_status=expected_status, jsonify=True)
        return response.get('name')

    def get_url(self):
        params = {
            'url': const.CAMPAIGN_URL
        }

        response = self._request('GET', locations.GET_URL, headers=self.headers(locations.REFERER_GET_URL),
                                 params=params, jsonify=True)
        return response.get('id')

    def post_load_file(self, file_path):
        file = {
            'file': open(file_path, 'rb'),
            'data': '{"width": 0, "height": 0}'
        }

        response = self._request('POST', locations.LOAD_FILE, headers=self.headers(locations.REFERER_LOAD_FILE),
                                 files=file, jsonify=True)
        return response.get('id')

    def post_create_campaign(self, campaign_name, file_path):
        image_id = self.post_load_file(file_path)
        url_id = self.get_url()

        data = json.dumps(self.campaign_structure(campaign_name, image_id, url_id))

        response = self._request('POST', locations.CREATE_CAMPAIGN,
                                 headers=self.headers(locations.REFERER_CREATE_CAMPAIGN), data=data, jsonify=True)
        return response.get('id')

    def get_delete_campaign(self, campaign_id):
        data = json.dumps([{
            'id': campaign_id,
            'status': 'deleted'
        }])

        response = self._request('POST', locations.DELETE_CAMPAIGN,
                                 headers=self.headers(locations.REFERER_DELETE_CAMPAIGN), data=data,
                                 expected_status=204)
        return response

    def get_campaign(self, campaign_id, expected_status):
        response = self._request('GET', locations.GET_CAMPAIGN.format(campaign_id),
                                 headers=self.headers(locations.REFERER_GET_CAMPAIGN.format(campaign_id)),
                                 expected_status=expected_status, jsonify=True)
        return response.get('name')

