import pytest
from base import ApiBase


class TestApi(ApiBase):
    @pytest.mark.API
    def test_create_campaign(self, target_object_names):
        campaign_id = self.create_campaign(target_object_names.campaign_name)
        self.delete_campaign(campaign_id)

    @pytest.mark.API
    def test_create_segment(self, target_object_names):
        self.create_segment(target_object_names.segment_name)

    @pytest.mark.API
    def test_delete_segment(self, target_object_names):
        segment_id = self.create_segment(target_object_names.segment_name)
        self.delete_segment(segment_id)