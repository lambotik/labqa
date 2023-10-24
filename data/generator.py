from faker import Faker

from data.data import Person

faker_ru = Faker('ru_RU')
faker_en = Faker('En')


def generated_person():
    """Generates random data using the Faker library."""
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )
