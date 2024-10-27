# Phase 4

import random
import time


class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance_traveled = 0

    def drive(self):
        self.distance_traveled += self.speed

    def change_speed(self):
        change = random.randint(-20, 20)
        self.speed = max(0, self.speed + change)

    def __str__(self):
        return f"{self.name:<20} | {self.speed:<10} | {self.distance_traveled:<15}"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.change_speed()
            car.drive()

    def print_status(self):
        print(f"\n{'Car Name':<20} | {'Speed (km/h)':<10} | {'Distance Traveled (km)':<15}")
        print("-" * 55)
        for car in self.cars:
            print(car)

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


def main():

    cars = [Car(f"Car {i + 1}") for i in range(10)]


    race = Race(name="Grand Demolition Derby", distance=8000, cars=cars)


    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1


        if hours_passed % 10 == 0:
            race.print_status()


    race.print_status()
    print(f"\nThe race is finished after {hours_passed} hours!")


if __name__ == "__main__":
    main()
