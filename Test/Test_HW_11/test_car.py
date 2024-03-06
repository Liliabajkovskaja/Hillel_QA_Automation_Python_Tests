import pytest


class TestCar:

    def test_miles_limit(self, car):
        assert car.miles_limit == 0

    def test_negative_miles_limit(self, car):
        with pytest.raises(AssertionError):
            assert car.miles_limit != 0

    def test_engine_started(self, car):
        assert car.start_engine() == "Engine started."

    def test_engine_started_true(self, car):
        car.start_engine()
        assert car._Car__is_engine_started == True

    def test_engine_started_false(self, car):
        car.start_engine()
        with pytest.raises(AssertionError):
            assert car._Car__is_engine_started == False

    def test_engine_is_already_running(self, car):
        car.start_engine()
        assert car.start_engine() == "Engine is already running."

    def test_stop_engine_check_text(self, car):
        car.start_engine()
        assert car.stop_engine() == "Engine stopped."

    def test_stop_engine_false(self, car):
        car.start_engine()
        car.stop_engine()
        assert car._Car__is_engine_started == False

    def test_stop_engine_is_already_off(self, car):
        car.stop_engine()
        assert car.stop_engine() == "Engine is already off."

    def test_drive_less_limit(self, car):
        car._Car__miles_limit = 100
        car.start_engine()
        assert car.drive(50) == "Driving 50 miles."

    def test_drive_more_limit(self, car):
        car._Car__miles_limit = 40
        car.start_engine()
        assert car.drive(50) == "The miles limit has been exceeded"

    def test_cannot_drive_ingine_off(self, car):
        assert car.drive(10) == "Cannot drive. Engine is off."
