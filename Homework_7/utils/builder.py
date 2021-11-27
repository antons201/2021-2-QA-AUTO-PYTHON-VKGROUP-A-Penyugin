from dataclasses import dataclass
import faker

fake = faker.Faker()


class Builder:
    @staticmethod
    def user(name=None, surname=None):

        @dataclass
        class User:
            name: str = None
            surname: str = None

        if name is None:
            name = fake.first_name()

        if surname is None:
            surname = fake.last_name()

        return User(name=name, surname=surname)
