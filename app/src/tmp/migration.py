from app.src.models.create import  LocalSession
from faker import Faker
from random import randint, choice
from sqlalchemy.orm import sessionmaker
from app.src.models.user import User, Team, Advert, Response, SimpleEmployee, CompanyEmployee  # Импорт моделей

# Создаем экземпляр Faker для генерации случайных данных
fake = Faker()
session = LocalSession()

# Генерация случайных данных для User
def create_random_users(num_users=5):
    users = []
    for _ in range(num_users):
        user = User(
            companyname=fake.company(),
            bio=fake.text(max_nb_chars=200),
            email=fake.email(),
            password_hash=fake.password(),# Опционально, если нужно логотип компании
        )
        session.add(user)
        users.append(user)
    session.commit()
    return users

# Генерация случайных данных для Team
def create_random_teams(num_teams=3, users=None):
    teams = []
    for _ in range(num_teams):
        team = Team(
            name=fake.bs(),
            user_id=choice(users).id  # Связь с случайным пользователем
        )
        session.add(team)
        teams.append(team)
    session.commit()
    return teams

# Генерация случайных данных для Advert
def create_random_adverts(num_adverts=10, users=None):
    adverts = []
    for _ in range(num_adverts):
        advert = Advert(
            advert_title=fake.job(),
            job=fake.job(),
            position=fake.job(),
            description=fake.text(max_nb_chars=300),
            user_id=choice(users).id  # Связь с случайным пользователем
        )
        session.add(advert)
        adverts.append(advert)
    session.commit()
    return adverts

# Генерация случайных данных для SimpleEmployee
def create_random_simple_employees(num_employees=10):
    employees = []
    for _ in range(num_employees):
        employee = SimpleEmployee(
            name=fake.first_name(),
            surname=fake.last_name(),
            number=fake.phone_number(),
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
            birth_time=fake.time(),
            birth_place="Atlanta",
            resume_url=fake.url(),
            bio=fake.text(max_nb_chars=200)
        )
        session.add(employee)
        employees.append(employee)
    session.commit()
    return employees

# Генерация случайных данных для CompanyEmployee
def create_random_company_employees(num_employees=10, users=None, teams=None):
    company_employees = []
    for _ in range(num_employees):
        employee = CompanyEmployee(
            name=fake.first_name(),
            surname=fake.last_name(),
            number=fake.phone_number(),
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
            birth_time=fake.time(),
            birth_place="Atlanta",
            resume_url=fake.url(),
            bio=fake.text(max_nb_chars=200),
            user_id=choice(users).id,
            team_id=choice(teams).id
        )
        session.add(employee)
        company_employees.append(employee)
    session.commit()
    return company_employees

# Генерация случайных данных для Response
def create_random_responses(num_responses=10, adverts=None, employees=None):
    responses = []
    for _ in range(num_responses):
        response = Response(
            emploee_id=choice(employees).id,
            advert_id=choice(adverts).id
        )
        session.add(response)
        responses.append(response)
    session.commit()
    return responses

# Заполнение базы данных
def start():
    # Генерируем случайных пользователей
    users = create_random_users(5)

    # Генерируем случайные команды
    teams = create_random_teams(3, users)

    # Генерируем рекламные объявления
    adverts = create_random_adverts(10, users)

    # Генерируем сотрудников (простых)
    simple_employees = create_random_simple_employees(20)

    # Генерируем сотрудников компании
    company_employees = create_random_company_employees(10, users, teams)

    # Генерируем отклики на объявления
    responses = create_random_responses(10, adverts, simple_employees)

    print("Данные успешно добавлены в базу!")

    # Закрытие сессии
    session.close()

