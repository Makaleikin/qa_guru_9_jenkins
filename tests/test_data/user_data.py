from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History: str = 'History'
    Maths: str = 'Maths'
    Physics: str = 'Pysics'


class Hobby(Enum):
    Sports: str = 'Sports'
    Reading: str = 'Reading'
    Music: str = 'Music'


class Gender(Enum):
    Male: str = 'Male'
    Female: str = 'Female'
    Other: str = 'Other'


@dataclass
class User:
    gender: Gender
    first_name: str = 'Artem'
    last_name: str = 'Mlynskij'
    email: str = 'listening@gmail.com'
    user_number: str = '0123456789'
    birth_day: str = '13'
    birth_month: str = 'October'
    birth_year: str = '1999'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths)
    hobbies: Tuple[Hobby] = Hobby.Sports
    current_address: str = 'The Earth'
    picture_file: str = 'test_data/qapicture.png'
    state: str = 'Haryana'
    city: str = 'Karnal'


student = User(first_name='Artem', gender=Gender.Male)
