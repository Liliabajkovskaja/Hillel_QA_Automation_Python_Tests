import pytest
from Lesson_15.Car import Car


@pytest.fixture()
def car():
    car = Car("Audi", "S8")
    yield car
    car._Car__miles_limit = 0
    car.stop_engine()
