from dataclasses import dataclass

import faker

fake = faker.Faker()


class Builder:
    @staticmethod
    def target_objects_names(campaign_name=None, segment_name=None):

        @dataclass
        class TargetObjectsNames:
            campaign_name: str = None
            segment_name: str = None

        if campaign_name is None:
            campaign_name = fake.lexify(text='??????? ???????? ?????????')

        if segment_name is None:
            segment_name = fake.lexify(text='????? ???? ? ?????? ????????')

        return TargetObjectsNames(campaign_name=campaign_name, segment_name=segment_name)
