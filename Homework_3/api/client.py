import json
from urllib.parse import urljoin

import requests


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.base_url = 'https://target.my.com/'
        self.email = 'testpenyugin@yandex.ru'
        self.password = 'testpass123$'

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

    def _request(self, method, location, headers=None, data=None, params=None, files=None, allow_redirects = False, expected_status=200, join_url = True, jsonify=False):
        if (join_url):
            url = urljoin(self.base_url, location)
        else:
            url = location

        response = self.session.request(method, url, headers=headers, data=data, params=params, files=files, allow_redirects=allow_redirects)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')

        if jsonify:
            json_response = response.json()
            return json_response

        return response

    def post_login(self):
        login_location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        continue_location = 'auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        headers = {
            'Referer': self.base_url
        }
        data = {
            'email': self.email,
            'password': self.password,
            'continue': urljoin(self.base_url, continue_location),
            'failure': 'https://account.my.com/login/'
        }

        response = self._request('POST', login_location, headers=headers, data=data, allow_redirects=True, join_url=False)

        self.mc = response.history[2].cookies.get('mc')
        self.sdc = response.history[4].cookies.get('sdc')

        self.get_csrftoken()

    def get_csrftoken(self):
        location = 'csrf/'
        headers = {
            'Referer': urljoin(self.base_url, 'dashboard')
        }

        response = self._request('GET', location, headers=headers, allow_redirects=True)

        self.csrf = response.cookies.get('csrftoken')

    def post_create_segment(self, segment_name):
        location = 'api/v2/remarketing/segments.json'
        referer_location = 'segments/segments_list/new'

        data = json.dumps(self.segment_structure(segment_name))

        response = self._request('POST', location, headers=self.headers(referer_location), data=data, jsonify=True)
        return response.get('id')

    def delete_delete_segment(self, segment_id):
        location = f'api/v2/remarketing/segments/{segment_id}.json'
        referer_location = 'segments/segments_list'

        response = self._request('DELETE', location, headers=self.headers(referer_location), expected_status=204)
        return response

    def get_segment(self, segment_id, expected_status):
        location = f'api/v2/remarketing/segments/{segment_id}.json'
        referer_location = f'segments/segments_list/{segment_id}'

        response = self._request('GET', location, headers=self.headers(referer_location), expected_status=expected_status)
        return response

    def get_url(self):
        location = 'api/v1/urls/'
        referer_location = 'campaign/new'

        params = {
            'url': 'https://mail.ru/'
        }

        response = self._request('GET', location, headers=self.headers(referer_location), params=params, jsonify=True)
        return response.get('id')

    def post_load_file(self, file_path):
        location = 'api/v2/content/static.json'
        referer_location = 'campaign/new'

        file = {
            'file': open(file_path, 'rb'),
            'data': '{"width": 0, "height": 0}'
        }

        response = self._request('POST', location, headers=self.headers(referer_location), files=file, jsonify=True)
        return response.get('id')

    def post_create_campaign(self, campaign_name, file_path):
        location = 'api/v2/campaigns.json'
        referer_location = 'campaign/new'
        image_id = self.post_load_file(file_path)
        url_id = self.get_url()

        data = json.dumps(self.campaign_structure(campaign_name, image_id, url_id))

        response = self._request('POST', location, headers=self.headers(referer_location), data=data, jsonify=True)
        return response.get('id')

    def get_delete_campaign(self, campaign_id):
        location = 'api/v2/campaigns/mass_action.json'
        referer_location = 'dashboard'

        data = json.dumps([{
            'id': campaign_id,
            'status': 'deleted'
        }])

        response = self._request('POST', location, headers=self.headers(referer_location), data=data, expected_status=204)
        return response

    def get_campaign(self, campaign_id, expected_status):
        location = f'api/v2/campaigns/{campaign_id}.json'
        referer_location = f'campaign/{campaign_id}?'

        response = self._request('GET', location, headers=self.headers(referer_location), expected_status=expected_status, jsonify=True)
        return response.get('name')

