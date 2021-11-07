import pytest

from utils.builder import Builder

class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, file_path):
        self.api_client = api_client
        self.builder = Builder()
        self.file_path = file_path

        self.api_client.post_login()

    @pytest.fixture()
    def target_object_names(self):
        target_object_names_data = self.builder.target_objects_names()
        yield target_object_names_data

    def create_campaign(self, campaign_name):
        campaign_id = self.api_client.post_create_campaign(campaign_name, self.file_path)
        assert self.api_client.get_campaign(campaign_id, 200) == campaign_name
        return campaign_id

    def delete_campaign(self, campaign_id):
        assert self.api_client.get_delete_campaign(campaign_id).status_code == 204

    def create_segment(self, segment_name):
        segment_id = self.api_client.post_create_segment(segment_name)
        assert self.api_client.get_segment(segment_id, 200).status_code == 200
        return segment_id

    def delete_segment(self, segment_id):
        assert self.api_client.delete_delete_segment(segment_id).status_code == 204
