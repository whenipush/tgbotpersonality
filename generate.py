from faker import Faker

fake = Faker('ru-ru')


def print_all():
    kek = f'Фио: {fake.name()}, \n ' \
          f'Адресc и индекс: {fake.address()} \n' \
          f'Дата рождения: {fake.date_of_birth(minimum_age=18)} \n' \
          f'Работа: {fake.job()} \n' \
          f'Город: {fake.city()} \n' \
          f'Телефон: {fake.phone_number()} \n'
    return kek


print(print_all())
