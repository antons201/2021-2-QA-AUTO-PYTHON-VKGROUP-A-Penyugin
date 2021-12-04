import pytest
from base import ApiBase


class TestApi(ApiBase):
    @pytest.mark.API
    def test_create_campaign(self, target_object_names):
        campaign_id = self.create_campaign(target_object_names.campaign_name)
        assert self.check_campaign(campaign_id, target_object_names.campaign_name)
        self.delete_campaign(campaign_id)

    @pytest.mark.API
    def test_create_segment(self, target_object_names):
        segment_id = self.create_segment(target_object_names.segment_name)
        assert self.check_segment(segment_id, target_object_names.segment_name)
        self.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self, target_object_names):
        segment_id = self.create_segment(target_object_names.segment_name)
        assert self.delete_segment(segment_id)
        assert not self.api_client.get_segment(segment_id, 404)
