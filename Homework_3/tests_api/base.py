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
        return campaign_id

    def delete_campaign(self, campaign_id):
        return self.api_client.get_delete_campaign(campaign_id)

    def create_segment(self, segment_name):
        segment_id = self.api_client.post_create_segment(segment_name)
        return segment_id

    def delete_segment(self, segment_id):
        return self.api_client.delete_delete_segment(segment_id)

    def check_campaign(self, campaign_id, campaign_name):
        return self.api_client.get_campaign(campaign_id, 200) == campaign_name

    def check_segment(self, segment_id, segment_name):
        return self.api_client.get_segment(segment_id, 200) == segment_name
