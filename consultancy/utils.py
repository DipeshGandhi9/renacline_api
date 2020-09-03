from enum import IntEnum


class Gender(IntEnum):
    MALE = 1
    FEMALE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class QuestionTypes(IntEnum):
    HOROSCOPE = 1
    MATCHMAKING = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
